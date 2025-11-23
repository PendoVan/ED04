from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, time, timedelta, date

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo

router = APIRouter(prefix="/disponibilidad", tags=["Disponibilidad"])


# -----------------------------------------------------------
# GENERAR FRANJAS DE 2 HORAS (10 → 18)
# -----------------------------------------------------------

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


# -----------------------------------------------------------
# DISPONIBILIDAD DE UNA FECHA (RESERVAS + BLOQUEOS)
# -----------------------------------------------------------

@router.get("/{fecha}")
def disponibilidad_por_fecha(fecha: str, db: Session = Depends(get_db)):
    """
    Retorna todas las franjas horarias de un día
    con su estado: disponible / reservado / bloqueado
    """

    # Validar fecha
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Formato de fecha inválido. Use YYYY-MM-DD")

    # Obtener reservas del día
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado == "reservado"
    ).all()

    # Obtener bloqueos del día
    bloqueos = db.query(Bloqueo).filter(
        Bloqueo.fecha == fecha_dt
    ).all()

    # Revisar si el día completo está bloqueado
    dia_bloqueado = any(b.tipo == "dia" for b in bloqueos)

    franjas = generar_franjas()
    respuesta = []

    for inicio, fin in franjas:
        estado = "disponible"

        # 1️⃣ SI TODO EL DÍA ESTÁ BLOQUEADO
        if dia_bloqueado:
            estado = "bloqueado"

        # 2️⃣ VERIFICAR BLOQUEO DE FRANJA
        for b in bloqueos:
            if b.tipo == "franja" and b.hora_inicio == inicio:
                estado = "bloqueado"

        # 3️⃣ VERIFICAR SI LA FRANJA ESTÁ RESERVADA
        for r in reservas:
            if r.hora_inicio == inicio:
                estado = "reservado"

        # registrar estado final
        respuesta.append({
            "inicio": inicio,
            "fin": fin,
            "estado": estado
        })

    return respuesta
