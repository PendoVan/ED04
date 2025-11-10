from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Reserva
from datetime import date

router = APIRouter(prefix="/reservas", tags=["Reservas"])

@router.get("/")
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(Reserva).all()

@router.post("/")
def crear_reserva(usuario: str, cancha: str, fecha: date, db: Session = Depends(get_db)):
    nueva = Reserva(usuario=usuario, cancha=cancha, fecha=fecha)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Reserva creada", "reserva": nueva}
