from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, time, timedelta, date
from typing import List, Dict

from backend.database import get_db
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo

router = APIRouter(prefix="/disponibilidad", tags=["Disponibilidad"])

def verificar_estado_rango(inicio_hora: int, fin_hora: int, reservas, bloqueos, dia_bloqueado):
    """
    Determina si un rango específico [inicio, fin) está libre.
    Retorna: 'Disponible', 'Reservado', 'Bloqueado'
    """
    if dia_bloqueado:
        return "Bloqueado"

    # Verificar superposición con bloqueos (de 1 hora)
    for b in bloqueos:
        b_ini = int(b.hora_inicio.split(":")[0])
        b_fin = int(b.hora_fin.split(":")[0])
        # Si hay overlap
        if inicio_hora < b_fin and fin_hora > b_ini:
            return "Bloqueado"

    # Verificar superposición con reservas (de 2 horas)
    for r in reservas:
        r_ini = int(r.hora_inicio.split(":")[0])
        r_fin = int(r.hora_fin.split(":")[0])
        if inicio_hora < r_fin and fin_hora > r_ini:
            return "Reservado"

    return "Disponible"

@router.get("/{fecha}")
def disponibilidad_por_fecha(fecha: str, rol: str = "student", db: Session = Depends(get_db)):
    """
    rol='student': devuelve franjas de 2h (10-12, 11-13...)
    rol='admin': devuelve franjas de 1h (10-11, 11-12...)
    """
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Formato inválido. Use YYYY-MM-DD")

    # Cargar datos del día
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado == "reservado"
    ).all()
    
    bloqueos = db.query(Bloqueo).filter(Bloqueo.fecha == fecha_dt).all()
    dia_bloqueado = any(b.tipo == "dia" for b in bloqueos)
    bloqueos_franja = [b for b in bloqueos if b.tipo == "franja"]

    respuesta = []
    apertura = 10
    cierre = 18

    if rol == "admin":
        # ADMIN: Franjas de 1 hora (10:00 - 18:00)
        for h in range(apertura, cierre):
            inicio = h
            fin = h + 1
            estado = verificar_estado_rango(inicio, fin, reservas, bloqueos_franja, dia_bloqueado)
            respuesta.append({
                "inicio": f"{inicio:02d}:00",
                "fin": f"{fin:02d}:00",
                "estado": estado
            })
    else:
        # ESTUDIANTE: Franjas de 2 horas deslizantes
        # Último inicio posible es 16:00 (para terminar 18:00)
        for h in range(apertura, cierre - 1):
            inicio = h
            fin = h + 2
            estado = verificar_estado_rango(inicio, fin, reservas, bloqueos_franja, dia_bloqueado)
            respuesta.append({
                "inicio": f"{inicio:02d}:00",
                "fin": f"{fin:02d}:00",
                "estado": estado
            })

    return respuesta