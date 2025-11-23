from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, time, timedelta, date

from backend.database import get_db
from backend.models.reserva import Reserva

router = APIRouter(prefix="/disponibilidad", tags=["Disponibilidad"])


def generar_franjas():
    """Genera franjas de 2 horas entre 10:00 y 18:00."""
    horas = []
    inicio = time(10, 0)
    fin = time(18, 0)

    actual = datetime.combine(date.today(), inicio)

    while actual.time() < fin:
        siguiente = actual + timedelta(hours=2)
        horas.append((
            actual.time().strftime("%H:%M"),
            siguiente.time().strftime("%H:%M")
        ))
        actual = siguiente

    return horas



@router.get("/{fecha}")
def disponibilidad_por_fecha(fecha: str, db: Session = Depends(get_db)):
    """
    Retorna las franjas horarias de un día con su estado:
    disponible / reservado / bloqueado
    """

    # Validar fecha
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Formato de fecha inválido. Use YYYY-MM-DD")

    # Obtener reservas del día
    reservas = db.query(Reserva).filter(Reserva.fecha == fecha_dt).all()

    franjas = generar_franjas()
    respuesta = []

    for inicio, fin in franjas:
        estado = "disponible"

        for r in reservas:
            if r.hora_inicio == inicio and r.hora_fin == fin:
                estado = "reservado"
                break

        respuesta.append({
            "inicio": inicio,
            "fin": fin,
            "estado": estado
        })

    return respuesta
