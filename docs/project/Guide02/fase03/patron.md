# Patron de Arquitectura de Software - Reserva de Loza Deportiva FISI

![ReservaFisi](https://github.com/user-attachments/assets/022e04ce-2945-45ba-9220-54ab4e14f221)

<div style="text-align: justify;">
El patrón de arquitectura en capas organiza el sistema en niveles bien definidos para separar responsabilidades y facilitar el mantenimiento. En el Sistema de Reservas FISI, 
la Capa de Presentación gestiona la interacción con el usuario a través del navegador web, mostrando interfaces como el calendario, el formulario de reserva y el inicio de sesión 
institucional. La Capa de Negocio concentra la lógica principal del sistema, donde los servicios de reserva, disponibilidad y notificación aplican las reglas definidas (validación de topes, bloqueos y horarios). Esta capa actúa como intermediaria entre la presentación y los datos, procesando las solicitudes y asegurando la coherencia del flujo. Finalmente, la Capa de Datos 
maneja la persistencia en MySQL, accediendo a la base mediante repositorios y gestionando conexiones con sistemas externos, como autenticación FISI y correo institucional.
Esta división garantiza modularidad, seguridad y la posibilidad de ampliar el sistema sin afectar otras partes, cumpliendo los principios de bajo acoplamiento y alta cohesión.
</div>

