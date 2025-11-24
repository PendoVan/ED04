# Seguimiento del Proyecto

El seguimiento del **Sistema de Reservas de Canchas FISI** se realizó mediante reuniones semanales, revisión de avances por fase y control de tareas en GitHub. A continuación se presenta el registro de seguimiento del proyecto.

---

## Metodología de Seguimiento

- **Reuniones semanales:** Cada lunes se realizaron reuniones presenciales o virtuales para revisar el avance de cada fase, identificar bloqueos y ajustar el cronograma.
- **Control de tareas:** Se utilizó GitHub Projects para gestionar tareas, asignar responsables y monitorear el progreso.
- **Revisión de entregables:** Cada fase fue revisada por el líder del proyecto antes de avanzar a la siguiente.

---

## Registro de Reuniones

### Reunión 01 — 2025-09-15
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Presentación del proyecto y objetivos del curso.
- Definición de roles y responsabilidades.
- Revisión de la Guía 01 y Guía 02.

**Acuerdos:**
- Martín Tapia: Líder de proyecto y Analista de requisitos.
- Piero Badillo: Desarrollador backend.
- Johan Reyes: Desarrollador frontend.
- Luis Gutierrez: Responsable de pruebas.

**Tareas asignadas:**
- Todos: Leer la Guía 01 y familiarizarse con el modelo Sashimi.
- Preparar: Preparar entrevista con el consejero de la facultad.

---

### Reunión 02 — 2025-09-29
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Revisión de la entrevista realizada con el consejero.
- Documentación de requisitos de usuario.
- Priorización de requisitos (mandatorios, mejoras, sin valor).

**Acuerdos:**
- Se priorizan 8 requisitos mandatorios para el MVP.
- RU-08 (aprobación manual) y RU-11 (externos/tarifa) se posponen como mejoras.

**Tareas asignadas:**
- Martín: Completar documentación de requisitos (RU, RF, RTM).
- Piero: Investigar FastAPI y Prisma ORM.
- Johan: Diseñar mockups de interfaces principales.

---

### Reunión 03 — 2025-10-13
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Revisión de mockups de interfaces.
- Definición de arquitectura en capas.
- Validación de requisitos funcionales.

**Acuerdos:**
- Se aprueba arquitectura en 3 capas: Presentación, Negocio, Datos.
- Se define patrón de arquitectura (Capas).
- Se valida la RTM (Requisitos ↔ RF ↔ CP).

**Tareas asignadas:**
- Piero: Iniciar desarrollo del backend (modelos, base de datos).
- Johan: Iniciar desarrollo del frontend (login, registro).
- Luis: Preparar casos de prueba basados en la RTM.

---

### Reunión 04 — 2025-10-20
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Revisión del avance del backend (autenticación, reservas).
- Revisión del avance del frontend (login, registro).
- Identificación de bloqueos técnicos.

**Bloqueos identificados:**
- Dificultad para conectar FastAPI con MySQL usando Prisma ORM.
- Se decide cambiar a SQLAlchemy ORM para facilitar la integración.

**Acuerdos:**
- Se aprueba el cambio a SQLAlchemy ORM.
- Se ajusta el cronograma para compensar el retraso.

**Tareas asignadas:**
- Piero: Migrar modelos de Prisma a SQLAlchemy.
- Johan: Continuar con frontend (pantalla de reservas).

---

### Reunión 05 — 2025-10-27
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Revisión de la integración backend-frontend.
- Validación de funcionalidades de reservas y disponibilidad.
- Preparación de casos de prueba.

**Acuerdos:**
- Se completa la integración del módulo de reservas.
- Se inicia el desarrollo del panel de administración.

**Tareas asignadas:**
- Piero: Implementar módulo de bloqueos (admin).
- Johan: Desarrollar panel de administración (frontend).
- Luis: Ejecutar casos de prueba CP-01 a CP-10.

---

### Reunión 06 — 2025-11-03
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Revisión de resultados de pruebas.
- Identificación de errores detectados.
- Planificación de correcciones.

**Errores detectados:**
- DEF-01: Selector de horarios no se deshabilitaba.
- DEF-03: Función de solapamiento rechazaba franjas consecutivas.
- DEF-05: Lista de reservas no se recargaba automáticamente.

**Acuerdos:**
- Se priorizan correcciones de errores de alta y media prioridad.

**Tareas asignadas:**
- Piero: Corregir DEF-03 (solapamiento).
- Johan: Corregir DEF-01 y DEF-05 (frontend).

---

### Reunión 07 — 2025-11-20
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Validación de correcciones de errores.
- Re-ejecución de casos de prueba.
- Preparación de documentación final.

**Acuerdos:**
- Todos los errores han sido corregidos exitosamente.
- Se aprueba el cierre de la fase de pruebas.

**Tareas asignadas:**
- Todos: Completar documentación de fases 04, 05 y 06.
- Martín: Preparar presentación final del proyecto.

---

### Reunión 08 — 2025-11-23
**Asistentes:** Martín Tapia, Piero Badillo, Johan Reyes, Luis Gutierrez  
**Agenda:**
- Revisión final de documentación.
- Preparación de presentación.
- Ensayo de demostración del sistema.

**Acuerdos:**
- Se aprueba la documentación completa del proyecto.
- Se prepara demo del sistema para la presentación final.

---

## Control de Avance por Fase

| Fase | Fecha Inicio | Fecha Fin Planificada | Fecha Fin Real | Estado | Observaciones |
|------|-------------|----------------------|----------------|--------|---------------|
| Fase 01: Requisitos | 2025-09-15 | 2025-09-22 | 2025-09-22 | ✅ Completado | Entrega a tiempo |
| Fase 02: Diseño de Artefactos | 2025-09-29 | 2025-09-29 | 2025-10-06 | ✅ Completado | Mockups aprobados |
| Fase 03: Análisis y Diseño | 2025-09-30 | 2025-10-06 | 2025-10-08 | ✅ Completado | Retraso de 2 días por cambio de ORM |
| Fase 04: Implementación | 2025-11-07 | 2025-11-22 | 2025-11-23 | ✅ Completado | Retraso de 1 día |
| Fase 05: Recursos HW/SW | 2025-11-10 | 2025-11-23 | 2025-11-22 | ✅ Completado | Adelanto de 1 día |
| Fase 06: Pruebas | 2025-11-21 | 2025-10-23 | 2025-10-23 | ✅ Completado | Todos los errores corregidos |
| Documentación Final | 2025-11-22 | 2025-11-23 | 2025-11-23 | ✅ Completado | Entrega a tiempo |

---

## Métricas del Proyecto

- **Total de requisitos identificados:** 10
- **Requisitos mandatorios implementados:** 7
- **Requisitos pospuestos:** 3
- **Total de casos de prueba ejecutados:** 19
- **Pruebas exitosas:** 18
- **Pruebas pendientes:** 1
- **Errores detectados:** 5
- **Errores corregidos:** 5
- **Tiempo total del proyecto:** 7 semanas

---

## Conclusión

El proyecto se completó exitosamente dentro del plazo establecido. Se implementaron todas las funcionalidades mandatorias del MVP y se corrigieron todos los errores detectados durante la fase de pruebas. La metodología de seguimiento semanal permitió identificar y resolver bloqueos técnicos de manera oportuna, garantizando la calidad del producto final.

