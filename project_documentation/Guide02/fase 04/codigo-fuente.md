# Código Fuente — Funciones Principales

A continuación se presenta el código fuente de las **funciones más importantes** del **Sistema de Reservas de Canchas FISI**, organizadas por módulo.

---

## 1. Autenticación — Login de Usuario

**Descripción:**  
Valida las credenciales del usuario y retorna su información (ID, correo, rol).

**Archivo:** `backend/routers/auth.py`
```python
@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    correo = data.correo.lower()

    # ADMIN
    if correo == ADMIN_CORREO:
        if data.password != ADMIN_PASSWORD:
            raise HTTPException(400, "Contraseña incorrecta para administrador.")

        admin = db.query(Usuario).filter(Usuario.correo == correo).first()
        if not admin:
            admin = Usuario(
                correo=correo,
                password_hash=ADMIN_PASSWORD,
                rol="admin"
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)

        return LoginResponse(id=admin.id, correo=admin.correo, rol=admin.rol)

    # ESTUDIANTE
    if not correo.endswith("@unmsm.edu.pe"):
        raise HTTPException(400, "El correo debe ser institucional.")

    user = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not user:
        raise HTTPException(400, "Usuario no registrado. Primero debe registrarse.")

    if data.password != user.password_hash:
        raise HTTPException(400, "Contraseña incorrecta.")

    return LoginResponse(id=user.id, correo=user.correo, rol=user.rol)
```

---

## 2. Reservas — Crear Reserva con Validaciones

**Descripción:**  
Crea una reserva aplicando todas las reglas de negocio: validación de disponibilidad, topes semanales, rango de días, solapamiento de franjas.

**Archivo:** `backend/routers/reservas.py`
```python
@router.post("/crear")
def crear_reserva(data: ReservaCreate, db: Session = Depends(get_db)):
    usuario_id = data.usuario_id
    fecha = data.fecha
    hora_inicio = data.hora_inicio

    # Validar usuario
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(404, "Usuario no encontrado")

    # Validar formato fecha
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Formato de fecha inválido. Use YYYY-MM-DD")

    hoy = date.today()

    # Validar que no sea fecha pasada
    if fecha_dt < hoy:
        raise HTTPException(400, "No puede reservar días pasados.")

    # Validar límite de 7 días
    if fecha_dt > hoy + timedelta(days=7):
        raise HTTPException(400, "Solo puede reservar hasta 7 días adelante.")

    # Validar franja válida
    if not rango_franja_valido(hora_inicio):
        raise HTTPException(400, "La franja debe ser una hora en punto entre 10:00 y 16:00")

    hora_fin = siguiente_hora(hora_inicio)

    # Validar hora pasada del mismo día
    if fecha_dt == hoy:
        hora_actual = datetime.now().hour
        inicio_int = int(hora_inicio.split(":")[0])
        if inicio_int < hora_actual:
            raise HTTPException(400, "No puede reservar horas que ya pasaron.")

    # Validar solapamiento
    reservas_dia = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado != "cancelado"
    ).all()

    h_ini_nueva = int(hora_inicio.split(":")[0])
    h_fin_nueva = int(hora_fin.split(":")[0])

    for r in reservas_dia:
        h_ini_exist = int(r.hora_inicio.split(":")[0])
        h_fin_exist = int(r.hora_fin.split(":")[0])

        if h_ini_nueva < h_fin_exist and h_ini_exist < h_fin_nueva:
            raise HTTPException(400, "Esa franja choca con una reserva existente.")

    # Validar máximo 2 reservas por semana
    semana_usuario = semana(fecha_dt)
    reservas_semana = db.query(Reserva).filter(
        Reserva.usuario_id == usuario_id,
        Reserva.estado == "reservado"
    ).all()

    count = 0
    for r in reservas_semana:
        if semana(r.fecha) == semana_usuario:
            count += 1

    if count >= 2:
        raise HTTPException(400, "Solo puede reservar máximo 2 veces por semana.")

    # Crear reserva
    nueva = Reserva(
        usuario_id=usuario_id,
        fecha=fecha_dt,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin,
        estado="reservado"
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return {
        "msg": "Reserva creada correctamente",
        "id": nueva.id,
        "fecha": fecha,
        "inicio": hora_inicio,
        "fin": hora_fin
    }
```

---

## 3. Disponibilidad — Consultar Disponibilidad

**Descripción:**  
Genera las franjas horarias del día y determina su estado (disponible, reservado, bloqueado).

**Archivo:** `backend/routers/disponibilidad.py`
```python
@router.get("/{fecha}")
def disponibilidad_fecha(fecha: str, db: Session = Depends(get_db)):

    # Validar fecha
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Formato inválido. Use YYYY-MM-DD.")

    franjas = generar_franjas()
    respuesta = []

    # Obtener reservas del día (excluyendo canceladas)
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado != "cancelado"
    ).all()

    # Obtener bloqueos del día
    bloqueos = db.query(Bloqueo).filter(Bloqueo.fecha == fecha_dt).all()

    # Detectar si el día está bloqueado completo
    dia_bloqueado = any(b.tipo == "dia" for b in bloqueos)

    for inicio, fin in franjas:
        estado = "disponible"

        # Si el día está bloqueado → todas las franjas bloqueadas
        if dia_bloqueado:
            estado = "bloqueado"

        # Revisar bloqueo por franja (solapamiento)
        if estado != "bloqueado":
            for b in bloqueos:
                if b.tipo == "franja":
                    b_fin = f"{int(b.hora_inicio.split(':')[0]) + 2}:00"
                    if hay_solapamiento(inicio, fin, b.hora_inicio, b_fin):
                        estado = "bloqueado"
                        break

        # Revisar si está reservado (solapamiento)
        if estado != "bloqueado":
            for r in reservas:
                if hay_solapamiento(inicio, fin, r.hora_inicio, r.hora_fin):
                    estado = "reservado"
                    break

        respuesta.append({
            "inicio": inicio,
            "fin": fin,
            "estado": estado
        })

    return respuesta
```

---

## 4. Administración — Bloquear Día Completo

**Descripción:**  
Bloquea todas las franjas de una fecha. Valida que no existan reservas activas antes de aplicar el bloqueo.

**Archivo:** `backend/routers/admin.py`
```python
@router.post("/bloquear_dia")
def bloquear_dia(fecha: str, db: Session = Depends(get_db)):

    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Fecha inválida. Use YYYY-MM-DD")

    # Verificar si hay reservas
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado == "reservado"
    ).all()

    if reservas:
        raise HTTPException(400, "No se puede bloquear un día con reservas activas.")

    # Verificar si ya está bloqueado
    existing = db.query(Bloqueo).filter(
        Bloqueo.fecha == fecha_dt,
        Bloqueo.tipo == "dia"
    ).first()

    if existing:
        raise HTTPException(400, "El día ya está bloqueado.")

    bloqueo = Bloqueo(
        fecha=fecha_dt,
        hora_inicio=None,
        hora_fin=None,
        tipo="dia"
    )

    db.add(bloqueo)
    db.commit()
    db.refresh(bloqueo)

    return {"msg": "Día bloqueado correctamente", "id": bloqueo.id}
```

---

## 5. Frontend — Cargar Disponibilidad y Crear Reserva

**Descripción:**  
Consulta la disponibilidad desde el frontend y permite seleccionar una franja para reservar.

**Archivo:** `frontend/js/reserva.js`
```javascript
async function cargarDisponibilidad() {
    const fecha = document.getElementById("fecha").value;
    const horarios = document.getElementById("horarios");

    horarios.innerHTML = "";
    horarios.disabled = false;

    if (!fecha) return;

    const lista = await apiDisponibilidad(fecha);

    // Contadores
    let disponibles = 0;
    let bloqueados = 0;
    let reservados = 0;
    let total = lista.length;

    lista.forEach(f => {
        if (f.estado === "disponible") disponibles++;
        if (f.estado === "bloqueado") bloqueados++;
        if (f.estado === "reservado") reservados++;
    });

    // 1. Caso: Día completamente bloqueado
    if (bloqueados === total && total > 0) {
        const opt = document.createElement("option");
        opt.textContent = "⚠️ Reservas bloqueadas para esta fecha";
        horarios.appendChild(opt);
        horarios.disabled = true;
        return;
    }

    // 2. Caso: Todo reservado
    if (disponibles === 0) {
        const opt = document.createElement("option");
        opt.textContent = "⚠️ Todas las franjas ya han sido reservadas.";
        horarios.appendChild(opt);
        horarios.disabled = true;
        return;
    }

    // 3. Caso normal: Mostrar disponibles
    lista.forEach(f => {
        if (f.estado === "disponible") {
            const opt = document.createElement("option");
            opt.value = `${f.inicio}|${f.fin}`;
            opt.textContent = `${f.inicio} - ${f.fin}`;
            horarios.appendChild(opt);
        }
    });

    if (horarios.children.length === 0) {
        const opt = document.createElement("option");
        opt.textContent = "No hay horarios disponibles.";
        horarios.appendChild(opt);
        horarios.disabled = true;
    }
}
```

---

## Conclusión

El código fuente presentado implementa las funcionalidades críticas del sistema: autenticación, creación de reservas con validaciones, consulta de disponibilidad y gestión de bloqueos administrativos. Todas las funciones aplican las reglas de negocio definidas en los requisitos funcionales.
