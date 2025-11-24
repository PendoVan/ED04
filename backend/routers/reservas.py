# backend/routers/reservas.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta
from typing import List

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.user import Usuario
from backend.models.bloqueo import Bloqueo
from backend.schema.reserva_schema import CrearReservaRequest, ReservaResponse
from backend.schema.reserva_schema import ReservaResponse as ReservaResponseModel

router = APIRouter(prefix="/reservas", tags=["Reservas"])

@router.post("/crear-simple", response_model=dict)
def crear_reserva_simple(
    usuario_id: int, 
    fecha: str, 
    hora_inicio: str, 
    db: Session = Depends(get_db)
):
    print(f"🔧 Datos recibidos: usuario_id={usuario_id}, fecha={fecha}, hora_inicio={hora_inicio}")
    try:
        try:
            fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            try:
                fecha_dt = datetime.strptime(fecha.split('T')[0], "%Y-%m-%d").date()
            except:
                raise HTTPException(400, "Formato fecha inválido")
        
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            raise HTTPException(404, "Usuario no encontrado")
        
        hora_limpia = hora_inicio.split(':')[0] + ':00'
        inicio_int = int(hora_limpia.split(':')[0])
        
        hoy = date.today()
        if fecha_dt < hoy:
            return {"error": "No se puede reservar en el pasado"}
        
        if not (10 <= inicio_int <= 16):
            return {"error": "Hora fuera de rango (10:00-16:00)"}
        
        fin_int = inicio_int + 2
        hora_fin = f"{fin_int:02d}:00"
        
        nueva = Reserva(
            usuario_id=usuario_id,
            fecha=fecha_dt,
            hora_inicio=hora_limpia,
            hora_fin=hora_fin,
            estado="reservado"
        )
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        
        return {"msg": "Reserva exitosa", "id": nueva.id}
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(500, f"Error: {str(e)}")

@router.post("/crear", response_model=dict)
def crear_reserva(reserva_data: CrearReservaRequest, db: Session = Depends(get_db)):
    usuario_id = reserva_data.usuario_id
    fecha = reserva_data.fecha
    hora_inicio = reserva_data.hora_inicio

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario: 
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha inválido. Use YYYY-MM-DD")

    hoy = date.today()
    ahora = datetime.now()

    if fecha_dt < hoy:
        raise HTTPException(status_code=400, detail="No se puede reservar en el pasado.")
    if fecha_dt > (hoy + timedelta(days=7)):
        raise HTTPException(status_code=400, detail="Solo se permite reservar con 1 semana de anticipación.")

    try:
        inicio_int = int(hora_inicio.split(":")[0])
    except (ValueError, IndexError):
        raise HTTPException(status_code=400, detail="Formato de hora inválido.")

    if fecha_dt == hoy and inicio_int <= ahora.hour:
        raise HTTPException(status_code=400, detail="Para el día de hoy, debe reservar con al menos 1 hora de anticipación.")

    if not (10 <= inicio_int <= 16):
        raise HTTPException(status_code=400, detail="Hora fuera de rango operativo (10:00 - 18:00)")

    fin_int = inicio_int + 2
    hora_fin = f"{fin_int:02d}:00"

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

    reservas_dia = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt, 
        Reserva.estado == "reservado"
    ).all()
    
    for r in reservas_dia:
        r_ini = int(r.hora_inicio.split(":")[0])
        r_fin = int(r.hora_fin.split(":")[0])
        if inicio_int < r_fin and fin_int > r_ini:
            raise HTTPException(400, "Conflicto: El horario se cruza con otra reserva.")

    bloqueos_dia = db.query(Bloqueo).filter(Bloqueo.fecha == fecha_dt).all()
    for b in bloqueos_dia:
        if b.tipo == "dia":
            raise HTTPException(400, "El día está completamente bloqueado por administración.")
        else:
            b_ini = int(b.hora_inicio.split(":")[0])
            b_fin = int(b.hora_fin.split(":")[0])
            if inicio_int < b_fin and fin_int > b_ini:
                raise HTTPException(400, "Conflicto: El horario choca con un bloqueo administrativo.")

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

@router.get("/mis-reservas/{usuario_id}", response_model=List[ReservaResponseModel])
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
