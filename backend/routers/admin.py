from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo

router = APIRouter(prefix="/admin", tags=["Administrador"])


# -----------------------------------------------------------
# UTILIDADES
# -----------------------------------------------------------

def validar_franja(hora: str):
    return hora in ["10:00", "12:00", "14:00", "16:00"]


def fin_franja(hora: str):
    h = int(hora.split(":")[0])
    return f"{h+2}:00"


# -----------------------------------------------------------
# 1️⃣ BLOQUEAR DÍA COMPLETO
# -----------------------------------------------------------

@router.post("/bloquear_dia")
def bloquear_dia(fecha: str, db: Session = Depends(get_db)):

    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Fecha inválida. Use YYYY-MM-DD")

    # Verificar si hay reservas
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado == "reservado"
    ).all()

    if reservas:
        raise HTTPException(400, "No se puede bloquear un día con reservas activas.")

    # Verificar si ya está bloqueado
    existing = db.query(Bloqueo).filter(
        Bloqueo.fecha == fecha_dt,
        Bloqueo.tipo == "dia"
    ).first()

    if existing:
        raise HTTPException(400, "El día ya está bloqueado.")

    bloqueo = Bloqueo(
        fecha=fecha_dt,
        hora_inicio=None,
        hora_fin=None,
        tipo="dia"
    )

    db.add(bloqueo)
    db.commit()
    db.refresh(bloqueo)

    return {"msg": "Día bloqueado correctamente", "id": bloqueo.id}


# -----------------------------------------------------------
# 2️⃣ BLOQUEAR UNA FRANJA HORARIA
# -----------------------------------------------------------

@router.post("/bloquear_franja")
def bloquear_franja(fecha: str, hora_inicio: str, db: Session = Depends(get_db)):
    
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Fecha inválida. Use YYYY-MM-DD")

    if not validar_franja(hora_inicio):
        raise HTTPException(400, "Franja inválida. Debe ser 10:00, 12:00, 14:00 o 16:00")

    hora_fin = fin_franja(hora_inicio)

    # Verificar que no esté reservada
    reserva = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.hora_inicio == hora_inicio,
        Reserva.estado == "reservado"
    ).first()

    if reserva:
        raise HTTPException(400, "No se puede bloquear una franja reservada.")

    # Verificar si ya está bloqueada
    bloqueo = db.query(Bloqueo).filter(
        Bloqueo.fecha == fecha_dt,
        Bloqueo.hora_inicio == hora_inicio
    ).first()

    if bloqueo:
        raise HTTPException(400, "La franja ya está bloqueada.")

    nuevo = Bloqueo(
        fecha=fecha_dt,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin,
        tipo="franja"
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return {"msg": "Franja bloqueada correctamente", "id": nuevo.id}


# -----------------------------------------------------------
# 3️⃣ VER BLOQUEOS DE UN DÍA
# -----------------------------------------------------------

@router.get("/bloqueos/{fecha}")
def obtener_bloqueos(fecha: str, db: Session = Depends(get_db)):
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Fecha inválida.")

    bloqueos = db.query(Bloqueo).filter(Bloqueo.fecha == fecha_dt).all()
    return bloqueos


# -----------------------------------------------------------
# 4️⃣ DESBLOQUEAR BLOQUEO
# -----------------------------------------------------------

@router.delete("/desbloquear/{bloqueo_id}")
def desbloquear(bloqueo_id: int, db: Session = Depends(get_db)):
    bloqueo = db.query(Bloqueo).filter(Bloqueo.id == bloqueo_id).first()
    if not bloqueo:
        raise HTTPException(404, "Bloqueo no encontrado")

    db.delete(bloqueo)
    db.commit()

    return {"msg": "Bloqueo eliminado correctamente"}
# admin router
