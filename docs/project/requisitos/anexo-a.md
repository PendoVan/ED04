# Anexo A — Técnicas de obtención de requisitos de software

## 1) Técnica utilizada
**Entrevista semiestructurada** a:
- **Consejero de la Facultad (rol Admin del proceso actual)**
- **Estudiantes/representantes** (usuarios finales)

Objetivo: identificar problemas del proceso actual y necesidades funcionales/no funcionales para el **MVP** del sistema de reservas de la cancha FISI.

## 2) Guion base
Contexto y flujo actual → Problemas → Funcionalidades indispensables → Reglas (franjas, topes, bloqueos) → Aprobación/notificaciones → Accesos (correo institucional) → Priorización.

## 3) Notas y evidencias (extracto)
**E1 — Flujo actual manual con 3 consejeros por WhatsApp, lista semanal a admins.**  
Se escribe por WhatsApp a uno de los tres consejeros; ellos consultan disponibilidad y el domingo consolidan y envían solicitudes.  
**Impacto:** justifica calendario centralizado.

**E2 — Problema principal: desorden y choques de reservas.**  
Reservas “independientes” se cruzan por falta de coordinación.  
**Impacto:** validación de regla anti-superposición y vista de agenda compartida.

**E3 — Qué debe ver el estudiante:**  
Disponibilidad/ocupación visible; los horarios ya reservados “en **rojo**”; requisito de **registro** para filtrar alumnos; si es **externo**, aplicar tarifa.  
**Impacto:** login institucional y UI con estados de franja.

**E4 — Automatización deseada para consejeros:**  
Una **lista ordenada (L–V)** de todas las reservas, lista para “subir”/gestionar.  
**Impacto:** reporte/consulta operativa para el consejo.

**E5 — Regla de tope por semana:**  
Máximo **dos reservas por semana** por grupo/base.  
**Impacto:** parámetro de negocio (topes por usuario/semana).

**E6 — Notificaciones para consejeros:**  
Alertas cuando se crea una reserva para no estar revisando manualmente.  
**Impacto:** notificaciones por evento.

**E7 — Acceso con correo institucional y código:**  
Autenticación con **correo institucional** y **código** para filtrar estudiantes vs. externos.  
**Impacto:** control de acceso y segmentación de tarifas.

**E8 — Top 3 funciones prioritarias:**  
1) **Registro/filtrado** de alumnos; 2) **Disponibilidad + pre-reserva** por el alumno; 3) **Tablero consolidado** para consejeros.  
**Impacto:** orden de implementación del MVP.

## 4) Conclusiones aplicadas
- Se prioriza un MVP con: calendario centralizado, auto-aprobación por reglas (sin choques), topes por semana, acceso institucional, y notificaciones.
- La tarifa para externos se registra a nivel de política/etiqueta; el pago en línea queda fuera de alcance en v1 (plan de mejora).

## 5) Trazabilidad RU ↔ Evidencia
| RU | Evidencia | Resumen |
|----|-----------|---------|
| RU-01 (ver disponibilidad con estados) | E3 | Ver libre/ocupado; ocupados en rojo. |
| RU-02 (reservar 1 franja) | E3/E8 | Pre-reserva por el alumno. |
| RU-03 (ver historial) | E3/E8 | Seguimiento del alumno. |
| RU-04 (cancelar) | E2 | Evitar choques/orden. |
| RU-05 (notificaciones usuario + consejeros) | E6 | Alerta por creación/estado. |
| RU-06 (parametrizar reglas y topes) | E5 | 2 por semana (parámetro). |
| RU-07 (bloqueos) | E1/E2 | Evitar choques/orden. |
| RU-09 (reportes) | E4 | Lista ordenada L–V. |
| RU-10 (login institucional + código) | E7 | Filtrar estudiantes vs. externos. |
| RU-11 (marcar externos y tarifa) | E3 | Registrar condición (sin pago online). |

## 6) Consideraciones éticas
Se informó uso académico de datos; sin datos sensibles; autorización si hay grabación.

## 7) Limitaciones
Una sola entrevista base; complementar con mini-encuesta y observación en la cancha.