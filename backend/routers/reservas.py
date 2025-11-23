from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.user import Usuario

router = APIRouter(prefix="/reservas", tags=["Reservas"])


# -------------------------------------------------------
# UTILIDADES
# -------------------------------------------------------

def rango_franja_valido(hora_inicio: str):
    """Valida que la franja esté dentro de las franjas permitidas."""
    franjas_validas = ["10:00", "12:00", "14:00", "16:00"]
    return hora_inicio in franjas_validas


def siguiente_hora(hora: str):
    h = int(hora.split(":")[0])
    return f"{h+2}:00"


def semana(fecha: date):
    """Devuelve la semana ISO (año, semana)."""
    return fecha.isocalendar()[:2]


# -------------------------------------------------------
# 1️⃣ CREAR RESERVA
# -------------------------------------------------------

@router.post("/crear")
def crear_reserva(usuario_id: int, fecha: str, hora_inicio: str, db: Session = Depends(get_db)):
    # Validar usuario
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(404, "Usuario no encontrado")

    # Validar formato fecha
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Formato de fecha inválido. Use YYYY-MM-DD")

    hoy = date.today()

    # Validar que no sea fecha pasada
    if fecha_dt < hoy:
        raise HTTPException(400, "No puede reservar días pasados.")

    # Validar límite de 7 días
    if fecha_dt > hoy + timedelta(days=7):
        raise HTTPException(400, "Solo puede reservar hasta 7 días adelante.")

    # Validar franja válida
    if not rango_franja_valido(hora_inicio):
        raise HTTPException(400, "La franja debe ser 10:00, 12:00, 14:00 o 16:00")

    hora_fin = siguiente_hora(hora_inicio)

    # Validar hora pasada del mismo día
    if fecha_dt == hoy:
        hora_actual = datetime.now().hour
        inicio_int = int(hora_inicio.split(":")[0])
        if inicio_int < hora_actual:
            raise HTTPException(400, "No puede reservar horas que ya pasaron.")

    # Validar que no exista ya una reserva en esa franja
    conflicto = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.hora_inicio == hora_inicio
    ).first()

    if conflicto:
        raise HTTPException(400, "Esa franja ya está reservada.")

    # Validar máximo 2 reservas por semana
    semana_usuario = semana(fecha_dt)
    reservas_semana = db.query(Reserva).filter(
        Reserva.usuario_id == usuario_id
    ).all()

    count = 0
    for r in reservas_semana:
        if semana(r.fecha) == semana_usuario:
            count += 1

    if count >= 2:
        raise HTTPException(400, "Solo puede reservar máximo 2 veces por semana.")

    # Crear reserva
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

    return {
        "msg": "Reserva creada correctamente",
        "id": nueva.id,
        "fecha": fecha,
        "inicio": hora_inicio,
        "fin": hora_fin
    }


# -------------------------------------------------------
# 2️⃣ LISTAR RESERVAS POR USUARIO
# -------------------------------------------------------

@router.get("/{usuario_id}")
def listar_reservas(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(404, "Usuario no encontrado")

    reservas = db.query(Reserva).filter(
        Reserva.usuario_id == usuario_id,
        Reserva.estado == "reservado"
    ).order_by(Reserva.fecha).all()

    return reservas


# -------------------------------------------------------
# 3️⃣ CANCELAR RESERVA
# -------------------------------------------------------

@router.delete("/{reserva_id}")
def cancelar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()

    if not reserva:
        raise HTTPException(404, "Reserva no encontrada")

    reserva.estado = "cancelado"
    db.commit()

    return {"msg": "Reserva cancelada correctamente"}

