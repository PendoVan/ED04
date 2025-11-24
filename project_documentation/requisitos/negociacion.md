# Negociación y acuerdos (MVP)

> Registro breve de decisiones para cerrar ambigüedades de la entrevista. Sirve de enlace RU→RF y como base de validación/RTM.

## N-01 Aprobación de reservas
- Opciones: manual por consejero / automática por reglas.
- **Decisión v1:** Automática si (franja libre ∧ no supera tope ∧ no cae en bloqueo).
- Justificación: reduce tiempos y carga operativa.
- Impacto: RF-02 (validar superposición y topes); pruebas CP-03..CP-06.

## N-02 Duración de franja
- Opciones: fija / variable por solicitud.
- **Decisión v1:** Fija **2 h**, **parametrizable** por Admin.
- Justificación: simplifica agenda; se ajusta a práctica actual.
- Impacto: RF-04 (CRUD reglas); CP de cálculo de disponibilidad.

## N-03 Topes por usuario
- Opciones: sin tope / 1 por día / 2 por semana / otro.
- **Decisión v1:** **1/día** y **2/semana** (parametrizable).
- Justificación: evita acaparamiento; pedido del consejero.
- Impacto: RF-02 (validaciones); casos de prueba de límite.

## N-04 Bloqueos del calendario
- Opciones: informativo / bloqueante.
- **Decisión v1:** **Bloqueante** (mantenimiento/feriados tienen prioridad).
- Justificación: previene choques.
- Impacto: RF-05 (CRUD bloqueos); CP de reserva en fecha bloqueada.

## N-05 Acceso y segmentación
- Opciones: acceso libre / correo institucional / extra con código.
- **Decisión v1:** **Correo institucional + código** (filtra estudiantes); externos marcados como tales.
- Justificación: control de acceso y diferenciar usuarios.
- Impacto: RF-07 (autenticación); RNF de seguridad básica.

## N-06 Tablero para consejeros
- Opciones: reporte posterior / vista operativa diaria.
- **Decisión v1:** **Listado L–V** con filtros básicos.
- Justificación: necesidad operativa clave.
- Impacto: RF-06 (listado/tabla); pruebas de filtrado/orden.
