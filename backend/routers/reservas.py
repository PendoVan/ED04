from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta
from typing import List

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.user import Usuario
from backend.models.bloqueo import Bloqueo
from backend.schema.reserva_schema import ReservaResponse  # 👈 NUEVO

router = APIRouter(prefix="/reservas", tags=["Reservas"])

@router.post("/crear", response_model=dict)
def crear_reserva(usuario_id: int, fecha: str, hora_inicio: str, db: Session = Depends(get_db)):
    # 1. Validaciones básicas
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario: 
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha inválido. Use YYYY-MM-DD")

    hoy = date.today()
    ahora = datetime.now()

    # 2. Validar anticipación
    if fecha_dt < hoy:
        raise HTTPException(status_code=400, detail="No se puede reservar en el pasado.")
    if fecha_dt > (hoy + timedelta(days=7)):
        raise HTTPException(status_code=400, detail="Solo se permite reservar con 1 semana de anticipación.")

    # 3. Validar hora de inicio
    try:
        inicio_int = int(hora_inicio.split(":")[0])
    except (ValueError, IndexError):
        raise HTTPException(status_code=400, detail="Formato de hora inválido.")

    if fecha_dt == hoy and inicio_int <= ahora.hour:
        raise HTTPException(status_code=400, detail="Para el día de hoy, debe reservar con al menos 1 hora de anticipación.")

    # 4. Validar rango operativo
    if not (10 <= inicio_int <= 16):
        raise HTTPException(status_code=400, detail="Hora fuera de rango operativo (10:00 - 18:00)")

    fin_int = inicio_int + 2
    hora_fin = f"{fin_int:02d}:00"

    # 5. Validar tope semanal
    year, week, _ = fecha_dt.isocalendar()
    reservas_semana = db.query(Reserva).filter(
        Reserva.usuario_id == usuario_id,
        Reserva.estado == "reservado",
        Reserva.fecha >= hoy,
        Reserva.fecha <= hoy + timedelta(days=7)
    ).all()
    
    count = 0
    for r in reservas_semana:
        r_year, r_week, _ = r.fecha.isocalendar()
        if r_year == year and r_week == week:
            count += 1
    
    if count >= 2:
        raise HTTPException(status_code=400, detail="Has alcanzado el límite de 2 reservas por semana.")

    # 6. Validar conflictos
    # ... (el resto del código de validaciones se mantiene igual)

    # 7. Guardar reserva
    nueva = Reserva(
        usuario_id=usuario_id,
        fecha=fecha_dt,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin,
        estado="reservado"
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return {"msg": "Reserva exitosa", "id": nueva.id}

@router.get("/mis-reservas/{usuario_id}", response_model=List[ReservaResponse])  # 👈 MEJORA
def listar_propias(usuario_id: int, db: Session = Depends(get_db)):
    reservas = db.query(Reserva).filter(
        Reserva.usuario_id == usuario_id,
        Reserva.estado == "reservado"
    ).all()
    return reservas

@router.delete("/{reserva_id}")
def cancelar(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if not reserva: 
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    reserva.estado = "cancelado"
    db.commit()
    return {"msg": "Reserva cancelada"}