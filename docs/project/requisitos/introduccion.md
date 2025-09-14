# Introducción — Requisitos (Guía 01)

**Proyecto:** Sistema web de reservas de la cancha FISI-UNMSM  
**Objetivo del sistema:** permitir a estudiantes y a la administración gestionar reservas por **franjas** de tiempo, con reglas y seguimiento.  
**Alcance de esta fase (Guía 01):** levantar requisitos de usuario, priorizarlos, negociar ambigüedades y dejar una especificación inicial validada.

## Partes interesadas
- **Estudiantes/Equipos:** realizan reservas, consultan disponibilidad, gestionan sus reservas.
- **Administrador (Deportes/Facultad):** define reglas (horarios, duración de franja, topes), bloqueos por mantenimiento/eventos, revisa métricas.
- **Docente supervisor:** revisa el avance documental y la trazabilidad.
- **Seguridad/Portería (opcional):** consulta el listado de reservas del día.

## Definiciones clave
- **Franja:** unidad de reserva. Para v1, **2 horas** por reserva (parámetro dado por el Administrador).
- **Bloqueo:** intervalo en el calendario no reservable (mantenimiento/evento).
