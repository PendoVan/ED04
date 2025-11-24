# Requisitos — Guía 01

**Proyecto:** Sistema web de reservas de cancha (FISI-UNMSM)  
**Alcance de esta carpeta:** Recolección, priorización y validación inicial de requisitos (Fase 01 de la Guía 01).  
**Última actualización:** 2025-09-14

---

## Contenido

- ➤ [Introducción](./introduccion.md) — contexto, actores y definiciones.
- ➤ [Requisitos de usuario](./requisitos-usuarios.md) — RU-xx por actor + supuestos.
- ➤ [Categorización](./categorizacion.md) — Mandatorio / Mejora / Sin valor.
- ➤ [Negociación](./negociacion.md) — acuerdos del MVP y trade-offs.
- ➤ [Validación](./validacion.md) — criterios (claridad, viabilidad, trazabilidad) y conclusiones.
- ➤ [RTM](./rtm.md) — Matriz de Trazabilidad RU ↔ RF ↔ CP.
- ➤ [Anexo A](./anexo-a.md) — técnica de obtención (entrevista), evidencias y hallazgos.

---

## Cómo leer esta sección (orden sugerido)

1. **Introducción** → actores, objetivo, glosario mínimo (p. ej., *franja*).
2. **Requisitos de usuario** → lista RU-xx por Estudiante/Admin/(Seguridad).
3. **Categorización** → marcar MVP (mandatorios) vs. mejoras.
4. **(Opcional) Negociación** → decisiones v1 (aprobación, topes, bloqueos…).
5. **Validación** → qué RU entran al avance y por qué; riesgos y acciones.
6. **RTM** → vincular RU-xx con RF-xx y CP-xx (para pruebas).
7. **Anexo A** → rastro de la entrevista y su impacto en los RU.

---

## Convenciones de IDs

- **RU-xx**: Requisito de Usuario (p. ej., RU-02 Reservar 1 franja).  
- **RF-xx**: Requisito Funcional (se referencian desde RTM).  
- **CP-xx**: Caso de Prueba (ver RTM/Validación).  
- **E#**: Evidencia de la entrevista en Anexo A (E1..E8).

---

## 🧩 Trazabilidad (RU → RF → CP)

> Ver el detalle completo en [rtm.md](./rtm.md). Aquí un resumen mínimo.

| RU (Requisito de Usuario)         | RF vinculados                 | CP vinculados (casos de prueba)                  |
|-----------------------------------|-------------------------------|--------------------------------------------------|
| RU-01 Disponibilidad              | RF-01 Listar franjas          | CP-01 Ver libres, CP-02 Feriados/Bloqueos        |
| RU-02 Reservar 1 franja           | RF-02 Crear reserva           | CP-03 No superposición, CP-05 Tope semanal       |
| RU-03 Ver/Cancelar mis reservas   | RF-03 Gestionar reservas      | CP-07 Ver mis reservas, CP-08 Cancelación        |
| RU-06 Reglas/Topes                | RF-04 CRUD Reglas             | CP-09 Cambiar franja, CP-10 Tope parametrizable  |
| RU-07 Bloqueos del calendario     | RF-05 CRUD Bloqueos           | CP-11 Reserva en fecha bloqueada                 |
| RU-09 Tablero consejeros (L–V)    | RF-06 Listado/Tablero         | CP-12 Orden y filtros                            |
| RU-11 Acceso institucional + código| RF-07 Autenticación           | CP-13 Login institucional                        |


- La **RTM** mantiene la trazabilidad viva y evita huecos (todo RU mandatorio debe tener al menos 1 RF y 1+ CP).

---

## ✅ Resumen del MVP (mandatorios)

Incluye, como mínimo:
- RU-01 Disponibilidad con estados
- RU-02 Reservar 1 franja
- RU-03 Ver mis reservas
- RU-04 Cancelar mi reserva
- RU-05 Notificaciones
- RU-06 Parametrizar reglas (duración, horarios, topes)
- RU-07 Bloqueos del calendario
- RU-09 Listado/Tablero para consejeros (L–V)
- RU-10 Acceso con correo institucional + código

> RU-08 (Aprobación manual) y RU-11 (externos/tarifa) quedan como **mejoras** del post-MVP.

---

## 🧪 Criterios de validación (resumen)

- **Claridad:** RU sin ambigüedad ni duplicidad.  
- **Viabilidad:** factible con los recursos y tiempo del avance.  
- **Trazabilidad:** RU ↔ RF ↔ CP y RU ↔ Evidencia (Anexo A).  
- **Testabilidad:** cada RU mandatorio tiene CP con resultado esperado.

---

## 🗒️ Changelog breve

- **2025-09-13:** Versión inicial del README de requisitos; índice, convenciones y trazabilidad añadidas.