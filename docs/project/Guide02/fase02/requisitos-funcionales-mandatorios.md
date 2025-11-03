## Descripción detallada de requisitos funcionales mandatorios del software

Este apartado ya fue trabajado en la sección "Requisitos funcionales" de:

[RTM de la Guía 01](https://github.com/PendoVan/ED04/blob/a074784db2d2e05fb7bae64e21d8072449055140/docs/project/requisitos/rtm.md)

# Matriz de Trazabilidad de Requisitos (RTM)

La matriz de trazabilidad asegura la relación entre los **Requisitos de Usuario (RU)**, los **Requisitos Funcionales (RF)** y los **Casos de Prueba (CP)** asociados. Esto garantiza cobertura, control de cambios y verificación del alcance del proyecto.

| Requisito de Usuario | Requisito Funcional asociado            | Casos de Prueba (CP) esperados | Observaciones |
|-----------------------|-----------------------------------------|-------------------------------|---------------|
| RU-01: Consultar disponibilidad | RF-01: Listar franjas por fecha aplicando reglas y bloqueos | CP-01: Mostrar franjas libres/ocupadas <br> CP-02: Reflejar bloqueos en calendario | Núcleo del sistema; validación visual en calendario. |
| RU-02: Reservar franja | RF-02: Crear reserva validando superposición y tope semanal | CP-03: Crear reserva válida <br> CP-04: Rechazar si supera 2/semana <br> CP-05: Rechazar si franja ocupada | Incluye validación de reglas de negocio. |
| RU-03: Ver historial/estado reservas <br> RU-04: Cancelar reserva | RF-03: Ver/cancelar reservas propias con política de cancelación | CP-06: Ver listado de reservas propias <br> CP-07: Cancelar si falta tiempo mínimo <br> CP-08: Rechazar cancelación fuera de plazo | Cancelación configurable (≥ N horas). |
| RU-05: Notificaciones | *(Se deriva de RF-02 y RF-03; función transversal)* | CP-09: Confirmación al crear <br> CP-10: Aviso al cancelar/rechazar | Asociado a eventos clave del flujo. |
| RU-06: Parametrizar reglas | RF-04: CRUD de reglas (duración, horarios, topes) | CP-11: Crear regla <br> CP-12: Editar regla <br> CP-13: Aplicar regla en validación de reservas | Reglas modificables sin despliegue. |
| RU-07: Bloqueos de calendario | RF-05: CRUD de bloqueos (mantenimiento/eventos) | CP-14: Registrar bloqueo <br> CP-15: Bloqueo impide reserva <br> CP-16: Editar/eliminar bloqueo | Los bloqueos tienen prioridad sobre reservas. |
| RU-09: Tablero operativo consejeros | RF-06: Tablero L–V con filtros básicos | CP-17: Mostrar reservas por semana <br> CP-18: Filtrar por estado <br> CP-19: Exportar listado simple | Enfocado en gestión semanal. |
| RU-10: Acceso institucional | *(Pospuesto; no habrá registro en v1)* | CP-20: Login válido con correo FISI <br> CP-21: Rechazar correo no institucional <br> CP-22: Marcar usuario externo | Seguridad y segmentación de usuarios. |
| RU-08: Aprobación manual (mejora) | *(Pospuesto; se integrará en versión futura)* | – | Auto-aprobación en v1; manual queda pendiente. |
| RU-11: Identificación externos (mejora) | *(Metadato; no implementa flujo en v1)* | – | Registro de externos, cobros fuera de alcance. |




