## Requisitos de Usuario

Este apartado ya fue trabajado en la 
[Guía 01 - Sección: Requisitos de Usuario](.../docs/project/requisitos/requisitos-usuarios.md).

Consulta y reutiliza ese contenido.

## Estudiante / Equipo
- **RU-01**: Consultar **disponibilidad** por fecha con estado visible de franjas (p. ej., ocupadas en rojo / libres en verde).
- **RU-02**: **Reservar 1 franja** (duración definida por la regla de negocio) en horario hábil.
- **RU-03**: **Ver** historial y estado de **mis reservas**.
- **RU-04**: **Cancelar** mi reserva antes del inicio de la franja.
- **RU-05**: **Recibir notificaciones** (creación/confirmación/rechazo/cancelación).

## Administrador / Consejo
- **RU-06**: **Parametrizar reglas**: duración de franja, horarios/días hábiles y **topes por usuario** (v1 sugerido: **2 reservas/semana**).
- **RU-07**: **Bloquear** fechas/horas (mantenimiento/eventos).
- **RU-08**: (Mejora) **Aprobación manual** bajo políticas específicas (v1: auto-aprobación por reglas).
- **RU-09**: **Vista/listado operativo** de reservas **ordenado (L–V)** para gestión del consejo.

## Acceso / Segmentación
- **RU-10**: **Acceso con correo institucional y código** para filtrar estudiantes de FISI.
- **RU-11**: **Identificar usuarios externos** y **marcar tarifa** asociada (registro de política; pago en línea fuera de alcance v1).

## Supuestos y restricciones (SRU)
- **SRU-01**: Sin **superposición** de reservas por usuario.
- **SRU-02**: El horario operativo y días hábiles son definidos por el Administrador.
- **SRU-03**: Duración de franja **no parametrizable**.
- **SRU-04**: MVP con **auto-aprobación por reglas**; la aprobación manual pasa a mejora.
