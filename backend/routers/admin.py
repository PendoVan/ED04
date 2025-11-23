from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/bloquear_franja")
def bloquear_franja(fecha: str, hora_inicio: str, db: Session = Depends(get_db)):
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Fecha inválida")

    # Admin bloquea de 1 en 1 hora
    ini_bloq = int(hora_inicio.split(":")[0])
    fin_bloq = ini_bloq + 1
    hora_fin = f"{fin_bloq:02d}:00"

    # Validar superposición con RESERVAS existentes (que duran 2h)
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt, 
        Reserva.estado == "reservado"
    ).all()

    for r in reservas:
        r_ini = int(r.hora_inicio.split(":")[0])
        r_fin = int(r.hora_fin.split(":")[0])
        
        # Si el bloqueo de 1h cae dentro de una reserva de 2h
        if ini_bloq < r_fin and fin_bloq > r_ini:
            raise HTTPException(400, "No se puede bloquear: existe una reserva en este horario.")

    # Validar si ya está bloqueado
    existente = db.query(Bloqueo).filter(
        Bloqueo.fecha == fecha_dt,
        Bloqueo.hora_inicio == hora_inicio,
        Bloqueo.tipo == "franja"
    ).first()
    
    if existente:
        raise HTTPException(400, "Esta franja ya está bloqueada.")

    nuevo = Bloqueo(
        fecha=fecha_dt,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin,
        tipo="franja"
    )
    db.add(nuevo)
    db.commit()
    
    return {"msg": "Franja bloqueada correctamente"}

@router.post("/bloquear_dia")
def bloquear_dia(fecha: str, db: Session = Depends(get_db)):
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Fecha inválida")

    # Solo si no hay reservas activas
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado == "reservado"
    ).first()
    
    if reservas:
        raise HTTPException(400, "No se puede bloquear el día: hay reservas activas.")

    bloqueo = Bloqueo(fecha=fecha_dt, tipo="dia")
    db.add(bloqueo)
    db.commit()
    return {"msg": "Día bloqueado exitosamente"}