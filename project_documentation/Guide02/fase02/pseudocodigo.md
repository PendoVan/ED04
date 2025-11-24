## Pseudocódigo de los requisitos de sistema más importantes (Requisitos funcionales mandatorios)

- En esta sección colocarán los pseudocódigos correspondientes a los requisitos funcionales más importantes del software.
- Mínimamente 02 pseudocodigos y máximo 03 pseudoodigos.

## RF-01: Consultar disponibilidad de canchas
El sistema debe permitir al usuario visualizar la disponibilidad de las canchas según la fecha, hora y tipo de cancha.

- Muestra calendario o listado de horarios libres y ocupados.
- Permite aplicar filtros (fecha, sede, tipo de superficie).
- Actualiza en tiempo real según nuevas reservas o bloqueos.

## Pseudocódigo de RF-01:
```
ALGORITMO ConsultarDisponibilidad
ENTRADA: fechaSeleccionada, tipoCancha

INICIO
  mostras "Consultar disponibilidad"
  listaCanchas <- obtenerCanchasDisponibles(fechaSeleccionada, tipoCancha)
      SI listaCanchas está vacía ENTONCES
          mostrar "No hay canchas disponibles para la fecha seleccionada"
      SINO
          PARA cada cancha EN listaCanchas HACER
              mostrar "Cancha:", cancha.nombre, 
                      " - Horario disponible:", cancha.horario
          FIN PARA
      FIN SI
  FIN
FIN ALGORITMO
```

## RF-02: Realizar una reserva
El sistema debe permitir reservar una cancha disponible registrando los datos del usuario y la franja horaria.

- Valida que la franja esté libre antes de confirmar.
- Calcula el costo de la reserva (si aplica).
- Envía confirmación o comprobante al usuario.

## Pseudocódigo de RF-02:
```
ALGORITMO RealizarReserva
ENTRADA: usuario, canchaSeleccionada, fecha, horaInicio, horaFin
INICIO
  SI verificarDisponibilidad(canchaSeleccionada, fecha, horaInicio, horaFin) = FALSO ENTONCES
    mostrar "Error: La cancha ya está reservada en ese horario"
  SALIR
    costo ← calcularCostoReserva(canchaSeleccionada, horaInicio, horaFin)
      mostrar "El costo de la reserva es: S/.", costo

      confirmar ← solicitarConfirmacionUsuario()

      SI confirmar = VERDADERO ENTONCES
          registrarReserva(usuario, canchaSeleccionada, fecha, horaInicio, horaFin, costo)
          enviarNotificacion(usuario, "Reserva confirmada con éxito")
          mostrar "Reserva registrada correctamente"
      SINO
          mostrar "Reserva cancelada por el usuario"
      FIN SI
  FIN
FIN ALGORITMO
```

## RF-03: Consultar y gestionar reservas
El sistema debe permitir al usuario ver, modificar o cancelar sus reservas activas.

- Lista todas las reservas realizadas.
- Permite cancelar con una política de tiempo mínimo (por ejemplo, 3 horas antes).
- Actualiza la disponibilidad al cancelar.

## Pseudocódigo de RF-03:
```
ALGORITMO GestionarReservas
ENTRADA: usuario
INICIO
  reservas ← obtenerReservasDelUsuario(usuario)
      SI reservas está vacía ENTONCES
        mostrar "No tienes reservas registradas"
      SINO
        mostrar "Tus reservas:"
          PARA cada reserva EN reservas HACER
            mostrar reserva.id, reserva.fecha, reserva.horaInicio, reserva.cancha
          FIN PARA

          opcion ← solicitarOpcionUsuario("Ver detalle / Cancelar / Salir")

          SEGÚN opcion HACER
              CASO "Ver detalle":
                  mostrarDetalleReserva(reservaSeleccionada)
              CASO "Cancelar":
                  SI validarTiempoCancelacion(reservaSeleccionada) = VERDADERO ENTONCES
                      cancelarReserva(reservaSeleccionada)
                      enviarNotificacion(usuario, "Reserva cancelada correctamente")
                      mostrar "Reserva cancelada"
                  SINO
                      mostrar "No es posible cancelar la reserva. Tiempo límite excedido."
                  FIN SI
              CASO "Salir":
                  mostrar "Saliendo del módulo de gestión."
          FIN SEGÚN
      FIN SI
  FIN
FIN ALGORITMO

```
