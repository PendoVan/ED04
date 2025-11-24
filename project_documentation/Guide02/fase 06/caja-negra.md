# Pruebas de Caja Negra

Las pruebas de caja negra se realizaron sobre los **requisitos funcionales mandatorios** del sistema. A continuación se presenta la **Matriz de Trazabilidad de Pruebas** que relaciona cada caso de prueba con su requisito funcional asociado.

---

## Matriz de Trazabilidad de Pruebas de Caja Negra

| ID Prueba | Requisito Funcional | Descripción del Caso de Prueba | Datos de Entrada | Resultado Esperado | Resultado Obtenido | Estado | Observaciones |
|-----------|---------------------|--------------------------------|------------------|--------------------|--------------------| -------|---------------|
| **CP-01** | RF-01: Listar franjas disponibles | Consultar disponibilidad de una fecha válida | Fecha: 2025-11-29 | Retorna lista de franjas con estados (disponible/reservado/bloqueado) | Lista de 7 franjas con estados correctos | ✅ PASS | <img width="708" height="637" alt="image" src="https://github.com/user-attachments/assets/4fe55037-a985-407c-9fab-bb611a637aa4" />|
| **CP-02** | RF-01: Reflejar bloqueos en calendario | Consultar disponibilidad de un día bloqueado completo | Fecha: 2025-11-28 (bloqueada) | Todas las franjas marcadas como "bloqueado" | Todas las franjas retornan estado "bloqueado" | ✅ PASS | <img width="684" height="508" alt="image" src="https://github.com/user-attachments/assets/ce70bc3f-e849-4460-a104-e5e8df2353d0" /> |
| **CP-03** | RF-02: Crear reserva válida | Crear reserva en franja disponible sin conflictos | Usuario: 1, Fecha: 2025-12-01, Hora: 10:00-12:00 | Reserva creada correctamente con ID asignado | Reserva ID 15 creada exitosamente | ✅ PASS | <img width="721" height="691" alt="image" src="https://github.com/user-attachments/assets/6d81cc51-fdbb-4663-8fdd-ebebb9a38ad0" /> |
| **CP-04** | RF-02: Rechazar si supera tope semanal | Crear reserva cuando el usuario ya tiene 2 reservas en la semana | Usuario: 1, Fecha: 2025-11-29, Hora: 14:00-16:00 | Error: "Solo puede reservar máximo 2 veces por semana" | Error HTTP 400 con mensaje correcto | ✅ PASS | <img width="714" height="683" alt="image" src="https://github.com/user-attachments/assets/85acc24b-814f-47ba-96e6-597ee8818332" /> |
| **CP-05** | RF-02: Rechazar si franja ocupada | Crear reserva en franja ya reservada | Usuario: 2, Fecha: 2025-11-28, Hora: 10:00 | Error: "Esa franja choca con una reserva existente" | Error HTTP 400 con mensaje correcto | ✅ PASS | <img width="684" height="508" alt="image" src="https://github.com/user-attachments/assets/ac0d7dcd-670a-4766-b50b-0663666f2be7" /> |
| **CP-06** | RF-03: Ver reservas propias | Listar reservas activas del usuario | Usuario ID: 1 | Lista de reservas del usuario con estado "reservado" | Retorna 2 reservas activas del usuario | ✅ PASS | <img width="1052" height="431" alt="image" src="https://github.com/user-attachments/assets/eb96954a-e96c-433b-b9f6-908819f53636" /> |
| **CP-07** | RF-03: Cancelar reserva | Cancelar una reserva activa | Reserva ID: 15 | Reserva pasa a estado "cancelado" | Reserva ID 15 cancelada exitosamente | ✅ PASS | <img width="1107" height="510" alt="image" src="https://github.com/user-attachments/assets/e9ba6d1a-c40a-4c42-8dcc-fc446e81578b" /> |
| **CP-08** | RF-03: Rechazar cancelación de reserva inexistente | Cancelar reserva que no existe | Reserva ID: 9999 | Error: "Reserva no encontrada" | Error HTTP 404 con mensaje correcto | ✅ PASS | — |
| **CP-09** | RF-04: Crear regla | *(Pospuesto para MVP; parametrización manual)* | — | — | — | ⏸️ PENDING | Funcionalidad no implementada en v1 |
| **CP-10** | RF-04: Aplicar regla en validación | Validar tope de 2 reservas/semana | Usuario: 1 (con 2 reservas previas) | Error al intentar reservar una tercera | Error HTTP 400 correcto | ✅ PASS | Regla aplicada correctamente |
| **CP-11** | RF-05: Registrar bloqueo día completo | Bloquear día completo sin reservas activas | Fecha: 2025-12-03 | Bloqueo creado correctamente | Bloqueo ID 3 creado exitosamente | ✅ PASS | <img width="1544" height="937" alt="image" src="https://github.com/user-attachments/assets/9db36132-95cc-4230-861e-8a45a461abe3" /> |
| **CP-12** | RF-05: Bloqueo impide reserva | Intentar reservar en día bloqueado | Fecha: 2025-11-27, Hora: 10:00 | Error: franja marcada como "bloqueada" | Consulta de disponibilidad retorna "bloqueado" | ✅ PASS | <img width="1536" height="916" alt="image" src="https://github.com/user-attachments/assets/94bfab90-1dcf-4fca-8dc0-a2f71162867e" /> |
| **CP-13** | RF-05: Bloquear franja específica | Bloquear franja horaria sin reservas | Fecha: 2025-11-29, Hora: 14:00 | Bloqueo de franja creado correctamente | Bloqueo ID 4 creado exitosamente | ✅ PASS | <img width="1509" height="909" alt="image" src="https://github.com/user-attachments/assets/2438b76d-2bbe-491f-8197-66d90e02ad05" /> |
| **CP-14** | RF-05: Rechazar bloqueo con reservas activas | Bloquear día que tiene reservas activas | Fecha: 2025-11-28 (con reservas) | Error: "No se puede bloquear un día con reservas activas" | Error HTTP 400 con mensaje correcto | ✅ PASS | <img width="1536" height="916" alt="image" src="https://github.com/user-attachments/assets/dc7983d8-a1ad-4f8f-ba69-5abbab69dd97" /> |
| **CP-15** | RF-06: Mostrar tablero de consejeros | Consultar disponibilidad desde panel admin | Fecha: 2025-11-28 | Tabla con estado de franjas (disponible/reservado/bloqueado) | Tabla renderizada correctamente en frontend | ✅ PASS | <img width="733" height="767" alt="image" src="https://github.com/user-attachments/assets/f94c15c1-322e-4114-85cc-75f401bbe458" /> |
| **CP-16** | RF-07: Login válido con correo institucional | Iniciar sesión con correo `@unmsm.edu.pe` | Correo: estudiante@unmsm.edu.pe, Password: 123 | Login exitoso, retorna ID, correo, rol | Login exitoso, ID: 1, rol: student | ✅ PASS | — |
| **CP-17** | RF-07: Rechazar correo no institucional | Iniciar sesión con correo externo | Correo: usuario@gmail.com | Error: "El correo debe ser institucional" | Error HTTP 400 con mensaje correcto | ✅ PASS | <img width="681" height="796" alt="image" src="https://github.com/user-attachments/assets/c5a8100c-bdbd-4bdb-8993-7871d5c9828b" /> |
| **CP-18** | RF-02: Rechazar reserva en fecha pasada | Crear reserva en fecha anterior a hoy | Fecha: 2025-11-21, Hora: 10:00 | Error: "No puede reservar días pasados" | Error HTTP 400 con mensaje correcto | ✅ PASS | <img width="693" height="679" alt="image" src="https://github.com/user-attachments/assets/30b8a066-ca3e-4e4f-85fd-b8dd0ec62935" /> |
| **CP-19** | RF-02: Rechazar reserva fuera de ventana de 7 días | Crear reserva a más de 7 días adelante | Fecha: 2025-12-12, Hora: 10:00 | Error: "Solo puede reservar hasta 7 días adelante" | Error HTTP 400 con mensaje correcto | ✅ PASS | <img width="666" height="688" alt="image" src="https://github.com/user-attachments/assets/0e837927-2d20-4503-9f4b-e807f3d44720" /> |
| **CP-20** | RF-02: Rechazar franja inválida | Crear reserva en horario no permitido | Hora: 09:00 (fuera de 10:00–16:00) | Error: "La franja debe ser una hora en punto entre 10:00 y 16:00" | Error HTTP 400 con mensaje correcto | ✅ PASS | <img width="703" height="679" alt="image" src="https://github.com/user-attachments/assets/e1bdcf57-83dc-4701-bf82-e1f54bfc0679" /> |

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

<img width="721" height="691" alt="image" src="https://github.com/user-attachments/assets/6d81cc51-fdbb-4663-8fdd-ebebb9a38ad0" />

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

<img width="714" height="683" alt="image" src="https://github.com/user-attachments/assets/85acc24b-814f-47ba-96e6-597ee8818332" />

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

<img width="1544" height="937" alt="image" src="https://github.com/user-attachments/assets/9db36132-95cc-4230-861e-8a45a461abe3" />

---

## Conclusión

Todas las pruebas de caja negra sobre los requisitos funcionales mandatorios han sido ejecutadas exitosamente. El sistema cumple con las validaciones definidas y rechaza correctamente los casos de error esperados. La única funcionalidad pendiente (CRUD de reglas) fue pospuesta intencionalmente para versiones futuras del sistema.

