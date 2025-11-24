from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo
from backend.schema.bloqueo_schema import (  # AGREGAR IMPORT
    BloqueoFranjaRequest, 
    BloqueoDiaRequest,
    BloqueoResponse
)

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/bloquear_franja", response_model=BloqueoResponse)  # USAR SCHEMA
def bloquear_franja(bloqueo_data: BloqueoFranjaRequest, db: Session = Depends(get_db)):
    try:
        fecha_dt = datetime.strptime(bloqueo_data.fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Fecha inválida")

    # Admin bloquea de 1 en 1 hora
    ini_bloq = int(bloqueo_data.hora_inicio.split(":")[0])
    fin_bloq = ini_bloq + 1
    hora_fin = f"{fin_bloq:02d}:00"

    # Validar superposición con RESERVAS existentes
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt, 
        Reserva.estado == "reservado"
    ).all()

    for r in reservas:
        r_ini = int(r.hora_inicio.split(":")[0])
        r_fin = int(r.hora_fin.split(":")[0])
        
        if ini_bloq < r_fin and fin_bloq > r_ini:
            raise HTTPException(400, "No se puede bloquear: existe una reserva en este horario.")

    # Validar si ya está bloqueado
    existente = db.query(Bloqueo).filter(
        Bloqueo.fecha == fecha_dt,
        Bloqueo.hora_inicio == bloqueo_data.hora_inicio,
        Bloqueo.tipo == "franja"
    ).first()
    
    if existente:
        raise HTTPException(400, "Esta franja ya está bloqueada.")

    nuevo = Bloqueo(
        fecha=fecha_dt,
        hora_inicio=bloqueo_data.hora_inicio,
        hora_fin=hora_fin,
        tipo="franja"
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    
    return nuevo  # Retornar el objeto para el schema

@router.post("/bloquear_dia", response_model=BloqueoResponse)
def bloquear_dia(bloqueo_data: BloqueoDiaRequest, db: Session = Depends(get_db)):
    try:
        fecha_dt = datetime.strptime(bloqueo_data.fecha, "%Y-%m-%d").date()
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
    db.refresh(bloqueo)
    
    return bloqueo  # Retornar el objeto