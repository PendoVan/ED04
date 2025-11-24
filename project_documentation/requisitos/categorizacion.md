# Categorización lógica de requisitos (Guía 01)

> Criterios: **Mandatorio** (imprescindible para el MVP), **Mejora** (aporta valor pero puede esperar), **Sin valor** (fuera de alcance v1 o no aporta al objetivo del curso).

## Mandatorios (MVP)
| ID    | Descripción breve | Evidencia (Anexo A) | Justificación |
|-------|------------------------------------------------------------------------|---------------------|---------------|
| RU-01 | Consultar **disponibilidad** con estados (libre/ocupado)              | E3                  | Núcleo del sistema para decidir reservas. |
| RU-02 | **Reservar 1 franja** (duración definida por regla)                   | E3, E8              | Operación principal; “pre-reserva por el alumno”. |
| RU-03 | **Ver** historial/estado de **mis reservas**                          | E3                  | Seguimiento del usuario. |
| RU-04 | **Cancelar** reserva antes del inicio                                  | E2                  | Orden; libera franja y evita choques. |
| RU-05 | **Notificaciones** (usuario y aviso a consejeros)                      | E6                  | Comunicación de eventos sin revisión manual constante. |
| RU-06 | **Parametrizar reglas** (duración, horarios, **topes** por semana)     | E5                  | Gobernanza; v1: 2 reservas/semana por usuario (parametrizable). |
| RU-07 | **Bloqueos** de calendario (mantenimiento/eventos)                     | E1, E2              | Evita choques; prioridad sobre solicitudes. |
| RU-09 | **Listado/Tablero** operativo para consejeros (ordenado L–V)           | E4, E8              | Prioridad del consejero; uno de los “top 3” de la entrevista. |
| RU-10 | **Acceso con correo institucional + código**                           | E7                  | Filtra estudiantes vs. externos; requisito de acceso. |

## Mejoras (post-MVP)
| ID    | Descripción breve | Evidencia | Motivo para posponer |
|-------|-------------------------------------------------------|----------|----------------------|
| RU-08 | **Aprobación manual** por consejeros                  | E5       | v1 funciona con **auto-aprobación por reglas**; manual complica flujo/tiempos. |
| RU-11 | **Identificar externos** y **marcar tarifa**          | E3       | Se registra como metadato; procesos de cobro quedan fuera de v1. |

## Sin valor (fuera de alcance v1)
| Ítem                                   | Motivo |
|----------------------------------------|--------|
| **Pagos en línea / pasarelas**         | No es objetivo de la guía ni del MVP; añade complejidad y riesgos. |
| Integraciones con sistemas externos     | No necesarias para validar el flujo principal. |

---

## Resumen del MVP (lo mínimo que debe “vivir”)
**RU-01, RU-02, RU-03, RU-04, RU-05, RU-06, RU-07, RU-09, RU-10**  
→ Con esto el alumno puede reservar ordenadamente; el consejo gobierna con reglas/bloqueos y ve su tablero; hay acceso institucional y notificaciones.

## Implicancias para RF (siguiente archivo)
- RF-01: Listar franjas por fecha aplicando reglas/bloqueos.  
- RF-02: Crear reserva (validación de superposición + tope semanal).  
- RF-03: Ver/cancelar reservas propias (con política de cancelación).  
- RF-04: CRUD de **reglas** (duración, horarios, topes).  
- RF-05: CRUD de **bloqueos** (mantenimiento/eventos).  
- RF-06: **Tablero** de consejeros (lista ordenada L–V con filtros básicos).  
- RF-07: **Autenticación institucional** (correo + código).

