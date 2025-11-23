from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.schema.reserva_schema import ReservaRequest, ReservaResponse

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.post("/", response_model=ReservaResponse)
def crear_reserva(data: ReservaRequest, db: Session = Depends(get_db)):
    
    # Validar rango horario
    hora_i = int(data.hora_inicio.split(":")[0])
    hora_f = int(data.hora_fin.split(":")[0])

    if hora_i < 10 or hora_f > 18:
        raise HTTPException(400, "Horario fuera del rango (10:00 - 18:00).")

    if hora_f - hora_i != 2:
        raise HTTPException(400, "Las reservas deben ser de 2 horas exactas.")

    # Crear reserva (provisional con usuario 1)
    nueva = Reserva(
        usuario_id=1,  # ← temporal, luego usaremos token o sesión
        fecha=data.fecha,
        hora_inicio=data.hora_inicio,
        hora_fin=data.hora_fin,
        estado="reservado"
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva
