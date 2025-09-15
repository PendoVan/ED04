# Validación de Requisitos

## Criterios aplicados
- **Claridad:** redacción comprensible, sin ambigüedades.
- **Consistencia:** no hay contradicciones entre RU, RF y SRU.
- **Viabilidad:** los requisitos son factibles en tiempo y recursos del curso.
- **Trazabilidad:** cada RU está vinculado con al menos un RF y CP (ver RTM).
- **Testabilidad:** todos los RF poseen criterios de aceptación verificables.

---

## Resultados de validación

- **Cobertura:** los RU mandatorios (RU-01 a RU-07, RU-09, RU-10) están plenamente trazados a RF y CP.  
- **Mejoras:** RU-08 y RU-11 se documentan pero se posponen para no afectar el flujo principal.  
- **No valor:** pagos en línea e integraciones externas fueron descartados en el MVP.  
- **Restricciones:** SRU-01 a SRU-04 están reflejadas en RF (validación de superposición, tope semanal, cancelación, auto-aprobación inicial).  
- **No se encontraron contradicciones** entre requisitos ni reglas.  

---

## Conclusiones

- El sistema definido es **factible y consistente** con el alcance del curso.  
- El **MVP cubre adecuadamente** las operaciones críticas: consulta de disponibilidad, reservas, cancelaciones, reglas, bloqueos, tablero de consejeros y acceso institucional.  
- La trazabilidad asegura que cada requisito pueda validarse mediante pruebas funcionales.  
- Se recomienda continuar con el **modelado conceptual (diagramas ER, casos de uso)** utilizando la RTM como insumo principal.
