# Respuesta a la Pregunta de Investigación  
## Sistema de Reservas de Canchas FISI – 2025-II

Se responde de manera abierta a la pregunta formulada en la guía de aprendizaje acerca de si es posible completar el desarrollo de un prototipo de software en tres meses aplicando un modelo de ciclo de vida específico, dentro del curso de “Procesos de Software”.

En nuestro caso, la metodología aplicada no fue un modelo en espiral formal ni tampoco un Scrum estricto. El desarrollo del Sistema de Reservas de Canchas FISI se llevó a cabo mediante una **combinación pragmática de tres enfoques**:  
1) **Scrum ligero**,  
2) **Modelo Iterativo**,  
3) **Sashimi (Cascada superpuesta)**.

Este enfoque híbrido surgió de las necesidades reales del proyecto: avanzar por fases obligatorias del curso, corregir errores sobre la marcha, superar riesgos técnicos (integración FastAPI–Prisma–MySQL, diseño de reglas de disponibilidad, validación del flujo BPMN) y refinar continuamente cada entrega.

El trabajo se organizó en **iteraciones cortas equivalentes a sprints**, donde en cada ciclo se completó un conjunto de entregables: análisis, diseño de casos de uso, BPMN, arquitectura, backend, frontend y pruebas. Sin embargo, a diferencia del Scrum tradicional, las fases **no fueron completamente secuenciales**: muchas de ellas se superpusieron. Mientras se refinaba el BPMN, se avanzaba en la arquitectura; mientras se ajustaba el modelo de datos, ya se implementaban rutas del backend. Esta superposición es característica del **modelo Sashimi**, que permite que las fases “se toquen” sin estar completamente cerradas.

Por otro lado, la estructura del proyecto mostró claramente un funcionamiento **iterativo**: cada entrega fue un incremento funcional, revisado, corregido y ampliado. Esto permitió que el prototipo evolucionara de forma progresiva sin necesidad de reescribir grandes partes del sistema. A diferencia del modelo en espiral, el análisis de riesgos fue **ligero y práctico**, centrado en problemas reales como dependencias rotas, errores ORM, incompatibilidades de MySQL, o fallas en la integración frontend-backend. No se siguió un proceso formal ni burocrático, sino un análisis inmediato y orientado a desbloquear el avance.

En este sentido, aunque el proyecto compartió con la Espiral la idea de **revisar riesgos en cada ciclo**, no cumplió con la carga documental, reuniones formales ni revisiones pesadas del modelo original de Boehm. Por eso, la metodología aplicada encaja mejor como una **variante ágil del modelo iterativo complementada con prácticas ligeras de Sashimi y Scrum**, adaptada a los tiempos y recursos de un contexto académico.

**Conclusión:**  
Sí es posible completar un prototipo funcional en tres meses aplicando una metodología híbrida como la que utilizamos. El uso de **Scrum ligero**, combinado con **iteraciones incrementales** y la **superposición controlada de fases propia del modelo Sashimi**, permitió avanzar rápidamente, corregir errores sobre la marcha y producir un prototipo coherente y completo sin la carga de un modelo en espiral formal. La metodología empleada se ajustó perfectamente al ritmo, al contexto y a las restricciones del curso de “Procesos de Software”.

---

**Elaborado por:** Equipo de Desarrollo 04 — Sistema de Reservas de Canchas FISI  
**Fecha:** Noviembre 2025  
**Curso:** Procesos de Software — FISI, UNMSM
