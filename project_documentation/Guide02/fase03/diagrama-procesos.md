
### Desarrollo del Diagrama de Procesos

El **proceso de reserva de cancha** del Sistema de Reservas FISI se compone de tres fases principales: **Solicitud**, **Verificación de disponibilidad** y **Confirmación**.  
El flujo inicia cuando el **usuario** accede al sistema, inicia sesión y selecciona la opción *Reservar cancha*. Posteriormente, el sistema permite elegir la fecha y hora deseada, activando el **subproceso de verificación de disponibilidad**.  

En dicho subproceso, el **sistema web** consulta los horarios registrados, aplica las reglas y bloqueos definidos por el administrador, y evalúa la disponibilidad de la cancha.  
Si no existen conflictos o topes, el sistema procede a **registrar la reserva** y enviar una **confirmación por correo electrónico** al usuario.  
En caso contrario, se notifica la falta de disponibilidad.  

Este flujo de trabajo refleja una secuencia ordenada y automatizada que garantiza la **eficiencia en la gestión de reservas**, manteniendo la integridad de las reglas establecidas por la institución y asegurando una **experiencia clara y confiable para el usuario**.

<img width="1266" height="713" alt="image" src="https://github.com/user-attachments/assets/e3fc034e-9573-4c66-b931-0f9ec85b4568" />

<img width="1246" height="536" alt="image" src="https://github.com/user-attachments/assets/91b22d47-a93c-4282-843b-7cb9d9d83e54" />

### Interpretación técnica del proceso

El diagrama implementa un **flujo BPMN estructurado**, donde las actividades se distribuyen entre los **roles de Usuario, Sistema Web y Administrador**.  
La inclusión del **subproceso de verificación de disponibilidad** permite modularizar la lógica del sistema, separando la interacción del usuario de la validación interna.  
Este diseño facilita la futura integración con otros módulos (como reportes o pagos externos) y garantiza una **arquitectura coherente con el patrón en capas**, en la cual el sistema mantiene un **bajo acoplamiento y alta cohesión** entre sus componentes funcionales.




