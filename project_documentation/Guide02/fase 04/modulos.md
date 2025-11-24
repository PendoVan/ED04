# Módulos del Sistema de Reservas FISI

El prototipo del **Sistema de Reservas de Canchas FISI** está organizado en módulos funcionales que permiten la gestión completa de reservas, disponibilidad, usuarios y administración. A continuación se describen los módulos implementados:

---

## 1. Módulo de Autenticación (`auth`)

**Descripción:**  
Gestiona el registro y el inicio de sesión de usuarios. Permite diferenciar entre estudiantes y administradores mediante roles.

**Funciones principales:**
- **Registro de estudiantes:** Validación de correo institucional (`@unmsm.edu.pe`) y creación de cuenta con rol `student`.
- **Login (estudiantes y administrador):** Verificación de credenciales y retorno de información del usuario (ID, correo, rol).
- **Credenciales de administrador fijas:** `adminfisi@unmsm.edu.pe` con contraseña `FISI2024`.

**Endpoint principal:**
- `POST /auth/registro` — Crear nueva cuenta de estudiante.
- `POST /auth/login` — Iniciar sesión (estudiante o admin).

**Archivo de implementación:**  
`backend/routers/auth.py`

---

## 2. Módulo de Reservas (`reservas`)

**Descripción:**  
Permite a los estudiantes crear, listar y cancelar reservas. Implementa las reglas de negocio principales del sistema: validación de superposición de franjas, límite de 2 reservas por semana, ventana de reserva de 7 días.

**Funciones principales:**
- **Crear reserva:** Validación de disponibilidad, topes semanales, rango de 7 días, franjas horarias válidas (10:00–16:00, duraciones de 2 horas).
- **Listar reservas propias:** Retorna las reservas activas del usuario.
- **Cancelar reserva:** Cambia el estado de la reserva a `cancelado`.

**Validaciones implementadas:**
- No permitir reservas en fechas pasadas.
- No permitir más de 2 reservas por semana por usuario.
- Detectar solapamiento de franjas (evita conflictos).
- Solo permitir reservar hasta 7 días adelante.

**Endpoints principales:**
- `POST /reservas/crear` — Crear nueva reserva.
- `GET /reservas/{usuario_id}` — Listar reservas del usuario.
- `DELETE /reservas/{reserva_id}` — Cancelar reserva.

**Archivo de implementación:**  
`backend/routers/reservas.py`

---

## 3. Módulo de Disponibilidad (`disponibilidad`)

**Descripción:**  
Consulta la disponibilidad de la cancha para una fecha específica. Genera automáticamente las franjas horarias y aplica los bloqueos y reservas existentes.

**Funciones principales:**
- **Generar franjas horarias:** Crea intervalos de 2 horas desde las 10:00 hasta las 18:00.
- **Verificar bloqueos:** Si el día está bloqueado completamente o si franjas específicas están bloqueadas, las marca como `bloqueado`.
- **Verificar reservas:** Marca las franjas ocupadas como `reservado`.
- **Detectar solapamiento:** Compara rangos de tiempo para determinar conflictos.

**Estados de franja:**
- `disponible` — La franja está libre.
- `reservado` — La franja ya tiene una reserva activa.
- `bloqueado` — La franja fue bloqueada por administrador (mantenimiento o evento).

**Endpoint principal:**
- `GET /disponibilidad/{fecha}` — Retorna la lista de franjas con su estado.

**Archivo de implementación:**  
`backend/routers/disponibilidad.py`

---

## 4. Módulo de Administración (`admin`)

**Descripción:**  
Permite a los administradores (consejeros) gestionar bloqueos del calendario. Los bloqueos tienen prioridad sobre las reservas y evitan que se reserven franjas durante mantenimiento o eventos especiales.

**Funciones principales:**
- **Bloquear día completo:** Bloquea todas las franjas de una fecha específica. Valida que no haya reservas activas antes de aplicar el bloqueo.
- **Bloquear franja específica:** Bloquea una franja horaria puntual (ej. 10:00–12:00). Valida que no esté reservada.
- **Ver bloqueos del día:** Retorna todos los bloqueos aplicados a una fecha.
- **Desbloquear:** Elimina un bloqueo existente.

**Reglas aplicadas:**
- No se puede bloquear una fecha o franja que tenga reservas activas.
- Los bloqueos se priorizan sobre las reservas en la consulta de disponibilidad.

**Endpoints principales:**
- `POST /admin/bloquear_dia` — Bloquear día completo.
- `POST /admin/bloquear_franja` — Bloquear franja específica.
- `GET /admin/bloqueos/{fecha}` — Ver bloqueos del día.
- `DELETE /admin/desbloquear/{bloqueo_id}` — Eliminar bloqueo.

**Archivo de implementación:**  
`backend/routers/admin.py`

---

## 5. Módulo de Base de Datos (`database`)

**Descripción:**  
Configura la conexión con la base de datos MySQL mediante SQLAlchemy. Provee la sesión de base de datos para los routers.

**Funciones principales:**
- Crear motor de base de datos.
- Proveer sesiones mediante `get_db()`.
- Crear tablas automáticamente al iniciar la aplicación.

**Archivo de implementación:**  
`backend/database/database.py`

---

## 6. Modelos de Datos (`models`)

**Descripción:**  
Define las entidades del sistema mediante SQLAlchemy ORM. Representa las tablas de la base de datos.

**Modelos implementados:**
- **Usuario (`user.py`):** Contiene correo, contraseña, rol (`student` o `admin`), y relación con reservas.
- **Reserva (`reserva.py`):** Contiene ID de usuario, fecha, hora de inicio, hora de fin, estado (`reservado` o `cancelado`).
- **Bloqueo (`bloqueo.py`):** Contiene fecha, hora de inicio, hora de fin, tipo (`dia` o `franja`).

**Archivos de implementación:**  
`backend/models/user.py`, `backend/models/reserva.py`, `backend/models/bloqueo.py`

---

## 7. Esquemas de Validación (`schema`)

**Descripción:**  
Define esquemas Pydantic para validar los datos de entrada y salida de las peticiones HTTP.

**Esquemas implementados:**
- **RegisterRequest, LoginRequest, LoginResponse** (`user_schema.py`)
- **ReservaCreate** (`reserva_schema.py`)
- **BloqueoCreate, BloqueoResponse** (`bloqueo_schema.py`)

**Archivos de implementación:**  
`backend/schema/`

---

## 8. Frontend (Interfaz de Usuario)

**Descripción:**  
Interfaz web construida con HTML, CSS y JavaScript Vanilla. Se comunica con el backend mediante `fetch` y renderiza dinámicamente los datos.

**Páginas implementadas:**
- **login.html** — Inicio de sesión.
- **registro.html** — Registro de estudiantes.
- **reservas.html** — Consulta de disponibilidad y creación de reservas.
- **mis_reservas.html** — Lista de reservas activas del estudiante.
- **admin_dashboard.html** — Panel de administración (gestión de bloqueos y consulta de disponibilidad).

**Archivos de implementación:**  
`frontend/`, `frontend/js/`

---

## Diagrama de Flujo de Módulos
```
Usuario (Estudiante/Admin)
         ↓
    Frontend (HTML/JS)
         ↓
    API REST (FastAPI)
         ↓
┌────────┴────────┐
│    Routers      │
├─────────────────┤
│ • auth          │
│ • reservas      │
│ • disponibilidad│
│ • admin         │
└────────┬────────┘
         ↓
    Models (SQLAlchemy)
         ↓
    Base de Datos (MySQL)
```

---

## Conclusión

El sistema está organizado en una arquitectura en capas, donde cada módulo tiene una responsabilidad específica. Esto facilita el mantenimiento, la escalabilidad y la trazabilidad de requisitos.
