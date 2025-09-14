# Requisitos de usuario

> **Técnica empleada para recopilar requisitos:** Entrevista semiestructurada al encargado del uso de la cancha y a estudiantes (ver [Anexo A](./anexo-a.md)).

## Ámbito funcional por parte interesada
- **Estudiante/Equipo**
  - Consultar disponibilidad por fecha y ver franjas libres/ocupadas.
  - Crear solicitud de reserva por una franja.
  - Ver/cancelar mis reservas.
  - Recibir notificaciones de creación, confirmación, rechazo y cancelación.
- **Administrador (Deportes/Facultad)**
  - Definir reglas del sistema: duración de franja, horarios y días hábiles, topes por usuario/semana.
  - Bloquear calendario por mantenimiento o eventos.
  - (Opcional v1) Aprobar/Rechazar solicitudes manualmente.
  - Reportes de uso (semanal/mensual).
- **Seguridad/Portería (opcional)**
  - Consultar listado de reservas del día para control de acceso.

## Requisitos de usuario (RU)
### Estudiante/Equipo
- **RU-01**: Consultar la **disponibilidad** por fecha (franjas libres/ocupadas).
- **RU-02**: **Crear una reserva** por **1 franja** (por defecto 2h) en horario hábil.
- **RU-03**: **Ver** el historial y el estado de **mis reservas**.
- **RU-04**: **Cancelar** una reserva propia antes del inicio de la franja.
- **RU-05**: **Recibir notificaciones** de creación/confirmación/rechazo/cancelación.

### Administrador
- **RU-06**: **Parametrizar reglas** (duración de franja, horarios/días hábiles, topes por usuario).
- **RU-07**: **Bloquear** fechas/horas (mantenimiento/eventos).
- **RU-08**: (Opcional v1) **Aprobar/Rechazar** solicitudes manualmente cuando la política lo requiera.
- **RU-09**: **Visualizar reportes** (uso, horas pico, tasa de rechazo).

### Seguridad/Portería (opcional)
- **RU-10**: Consultar **listado de reservas del día** (con identificador/QR).

## Supuestos y restricciones del usuario (SRU)
- **SRU-01**: Una reserva ocupa **exactamente 1 franja** (2h por defecto); no se permiten superposiciones por usuario.
- **SRU-02**: **Horario operativo** y **días hábiles** definidos por el Administrador.
- **SRU-03**: v1 gestiona **una cancha**; extensible a múltiples canchas a futuro.

---

## Resumen de la técnica aplicada y hallazgos (acople con el Anexo)
- **Técnica**: Entrevista semiestructurada (ver guion, notas y evidencias en [Anexo A](./anexo-a.md)).
- **Hallazgos clave**:
  - La **franja estándar es de 2 horas** y debe ser **parametrizable**.
  - Se requiere **evitar superposiciones** y poner **topes por usuario** (p. ej. 1 por día / 2 por semana).
  - El **bloqueo de fechas** por mantenimiento/eventos es prioritario sobre nuevas reservas.
  - La **aprobación manual** puede postergarse para una versión posterior; **auto-aprobación por reglas** en v1.
- **Trazabilidad preliminar** (RU ↔ Evidencia de entrevista):
  - RU-01, RU-02 → E1, E2 (necesidad de ver disponibilidad y reservar una franja).
  - RU-06, RU-07 → E3 (parametrización y bloqueos).
  - RU-03, RU-04, RU-05 → E4 (gestión básica del usuario y notificaciones).
