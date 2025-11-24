# Pruebas de Caja Negra

Las pruebas de caja negra se realizaron sobre los **requisitos funcionales mandatorios** del sistema. A continuación se presenta la **Matriz de Trazabilidad de Pruebas** que relaciona cada caso de prueba con su requisito funcional asociado.

---

## Matriz de Trazabilidad de Pruebas de Caja Negra

| ID Prueba | Requisito Funcional | Descripción del Caso de Prueba | Datos de Entrada | Resultado Esperado | Resultado Obtenido | Estado | Observaciones |
|-----------|---------------------|--------------------------------|------------------|--------------------|--------------------| -------|---------------|
| **CP-01** | RF-01: Listar franjas disponibles | Consultar disponibilidad de una fecha válida | Fecha: 2025-11-28 | Retorna lista de franjas con estados (disponible/reservado/bloqueado) | Lista de 7 franjas con estados correctos | ✅ PASS | — |
| **CP-02** | RF-01: Reflejar bloqueos en calendario | Consultar disponibilidad de un día bloqueado completo | Fecha: 2025-11-30 (bloqueada) | Todas las franjas marcadas como "bloqueado" | Todas las franjas retornan estado "bloqueado" | ✅ PASS | — |
| **CP-03** | RF-02: Crear reserva válida | Crear reserva en franja disponible sin conflictos | Usuario: 1, Fecha: 2025-11-28, Hora: 10:00 | Reserva creada correctamente con ID asignado | Reserva ID 15 creada exitosamente | ✅ PASS | — |
| **CP-04** | RF-02: Rechazar si supera tope semanal | Crear reserva cuando el usuario ya tiene 2 reservas en la semana | Usuario: 1, Fecha: 2025-11-29, Hora: 12:00 | Error: "Solo puede reservar máximo 2 veces por semana" | Error HTTP 400 con mensaje correcto | ✅ PASS | — |
| **CP-05** | RF-02: Rechazar si franja ocupada | Crear reserva en franja ya reservada | Usuario: 2, Fecha: 2025-11-28, Hora: 10:00 | Error: "Esa franja choca con una reserva existente" | Error HTTP 400 con mensaje correcto | ✅ PASS | — |
| **CP-06** | RF-03: Ver reservas propias | Listar reservas activas del usuario | Usuario ID: 1 | Lista de reservas del usuario con estado "reservado" | Retorna 2 reservas activas del usuario | ✅ PASS | — |
| **CP-07** | RF-03: Cancelar reserva | Cancelar una reserva activa | Reserva ID: 15 | Reserva pasa a estado "cancelado" | Reserva ID 15 cancelada exitosamente | ✅ PASS | — |
| **CP-08** | RF-03: Rechazar cancelación de reserva inexistente | Cancelar reserva que no existe | Reserva ID: 9999 | Error: "Reserva no encontrada" | Error HTTP 404 con mensaje correcto | ✅ PASS | — |
| **CP-09** | RF-04: Crear regla | *(Pospuesto para MVP; parametrización manual)* | — | — | — | ⏸️ PENDING | Funcionalidad no implementada en v1 |
| **CP-10** | RF-04: Aplicar regla en validación | Validar tope de 2 reservas/semana | Usuario: 1 (con 2 reservas previas) | Error al intentar reservar una tercera | Error HTTP 400 correcto | ✅ PASS | Regla aplicada correctamente |
| **CP-11** | RF-05: Registrar bloqueo día completo | Bloquear día completo sin reservas activas | Fecha: 2025-12-01 | Bloqueo creado correctamente | Bloqueo ID 3 creado exitosamente | ✅ PASS | — |
| **CP-12** | RF-05: Bloqueo impide reserva | Intentar reservar en día bloqueado | Fecha: 2025-12-01, Hora: 10:00 | Error: franja marcada como "bloqueada" | Consulta de disponibilidad retorna "bloqueado" | ✅ PASS | — |
| **CP-13** | RF-05: Bloquear franja específica | Bloquear franja horaria sin reservas | Fecha: 2025-11-28, Hora: 14:00 | Bloqueo de franja creado correctamente | Bloqueo ID 4 creado exitosamente | ✅ PASS | — |
| **CP-14** | RF-05: Rechazar bloqueo con reservas activas | Bloquear día que tiene reservas activas | Fecha: 2025-11-28 (con reservas) | Error: "No se puede bloquear un día con reservas activas" | Error HTTP 400 con mensaje correcto | ✅ PASS | — |
| **CP-15** | RF-06: Mostrar tablero de consejeros | Consultar disponibilidad desde panel admin | Fecha: 2025-11-28 | Tabla con estado de franjas (disponible/reservado/bloqueado) | Tabla renderizada correctamente en frontend | ✅ PASS | — |
| **CP-16** | RF-07: Login válido con correo institucional | Iniciar sesión con correo `@unmsm.edu.pe` | Correo: estudiante@unmsm.edu.pe, Password: 123 | Login exitoso, retorna ID, correo, rol | Login exitoso, ID: 1, rol: student | ✅ PASS | — |
| **CP-17** | RF-07: Rechazar correo no institucional | Iniciar sesión con correo externo | Correo: usuario@gmail.com | Error: "El correo debe ser institucional" | Error HTTP 400 con mensaje correcto | ✅ PASS | — |
| **CP-18** | RF-02: Rechazar reserva en fecha pasada | Crear reserva en fecha anterior a hoy | Fecha: 2025-11-01, Hora: 10:00 | Error: "No puede reservar días pasados" | Error HTTP 400 con mensaje correcto | ✅ PASS | — |
| **CP-19** | RF-02: Rechazar reserva fuera de ventana de 7 días | Crear reserva a más de 7 días adelante | Fecha: 2025-12-10, Hora: 10:00 | Error: "Solo puede reservar hasta 7 días adelante" | Error HTTP 400 con mensaje correcto | ✅ PASS | — |
| **CP-20** | RF-02: Rechazar franja inválida | Crear reserva en horario no permitido | Hora: 09:00 (fuera de 10:00–16:00) | Error: "La franja debe ser una hora en punto entre 10:00 y 16:00" | Error HTTP 400 con mensaje correcto | ✅ PASS | — |

---

## Resumen de Resultados

- **Total de pruebas ejecutadas:** 19
- **Pruebas exitosas (PASS):** 18
- **Pruebas pendientes (PENDING):** 1 (CRUD de reglas, pospuesto para MVP)
- **Pruebas fallidas (FAIL):** 0

---

## Evidencias de Pruebas

### CP-03: Crear reserva válida

**Request:**
```json
POST /reservas/crear
{
  "usuario_id": 1,
  "fecha": "2025-11-28",
  "hora_inicio": "10:00"
}
```

**Response:**
```json
{
  "msg": "Reserva creada correctamente",
  "id": 15,
  "fecha": "2025-11-28",
  "inicio": "10:00",
  "fin": "12:00"
}
```

![CP-03 Screenshot](./evidencias/cp03_reserva_valida.png)

---

### CP-04: Rechazar si supera tope semanal

**Request:**
```json
POST /reservas/crear
{
  "usuario_id": 1,
  "fecha": "2025-11-29",
  "hora_inicio": "12:00"
}
```

**Response:**
```json
{
  "detail": "Solo puede reservar máximo 2 veces por semana."
}
```

![CP-04 Screenshot](./evidencias/cp04_tope_semanal.png)

---

### CP-11: Bloquear día completo

**Request:**
```json
POST /admin/bloquear_dia?fecha=2025-12-01
```

**Response:**
```json
{
  "msg": "Día bloqueado correctamente",
  "id": 3
}
```

![CP-11 Screenshot](./evidencias/cp11_bloquear_dia.png)

---

### CP-16: Login válido

**Request:**
```json
POST /auth/login
{
  "correo": "estudiante@unmsm.edu.pe",
  "password": "123"
}
```

**Response:**
```json
{
  "id": 1,
  "correo": "estudiante@unmsm.edu.pe",
  "rol": "student"
}
```

![CP-16 Screenshot](./evidencias/cp16_login_valido.png)

---

## Conclusión

Todas las pruebas de caja negra sobre los requisitos funcionales mandatorios han sido ejecutadas exitosamente. El sistema cumple con las validaciones definidas y rechaza correctamente los casos de error esperados. La única funcionalidad pendiente (CRUD de reglas) fue pospuesta intencionalmente para versiones futuras del sistema.
