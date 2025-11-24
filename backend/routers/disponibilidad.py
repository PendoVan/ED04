from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date, time, timedelta

from backend.database.database import get_db
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo

router = APIRouter(prefix="/disponibilidad", tags=["Disponibilidad"])


# ----------------------------------------------
# Generador de franjas
# ----------------------------------------------
def generar_franjas():
    franjas = []
    # Franjas cada hora desde las 10:00 hasta las 16:00 (cierre 18:00)
    # 10-12, 11-13, 12-14, 13-15, 14-16, 15-17, 16-18
    hora = 10
    while hora <= 16:
        inicio = f"{hora:02d}:00"
        fin = f"{hora + 2:02d}:00"
        franjas.append((inicio, fin))
        hora += 1
    return franjas


def hay_solapamiento(inicio1: str, fin1: str, inicio2: str, fin2: str) -> bool:
    """Devuelve True si los intervalos se solapan."""
    # Convertir a enteros para comparar (solo hora)
    h_ini1 = int(inicio1.split(":")[0])
    h_fin1 = int(fin1.split(":")[0])
    h_ini2 = int(inicio2.split(":")[0])
    h_fin2 = int(fin2.split(":")[0])

    return h_ini1 < h_fin2 and h_ini2 < h_fin1


# ----------------------------------------------
# Endpoint principal
# ----------------------------------------------
@router.get("/{fecha}")
def disponibilidad_fecha(fecha: str, db: Session = Depends(get_db)):

    # Validar fecha
    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(400, "Formato inválido. Use YYYY-MM-DD.")

    franjas = generar_franjas()
    respuesta = []

    # Obtener reservas del día (excluyendo canceladas)
    reservas = db.query(Reserva).filter(
        Reserva.fecha == fecha_dt,
        Reserva.estado != "cancelado"
    ).all()

    # Obtener bloqueos del día
    bloqueos = db.query(Bloqueo).filter(Bloqueo.fecha == fecha_dt).all()

    # Detectar si el día está bloqueado completo
    dia_bloqueado = any(b.tipo == "dia" for b in bloqueos)

    for inicio, fin in franjas:
        estado = "disponible"

        # Si el día está bloqueado → todas las franjas bloqueadas
        if dia_bloqueado:
            estado = "bloqueado"

        # Revisar bloqueo por franja (solapamiento)
        if estado != "bloqueado":
            for b in bloqueos:
                if b.tipo == "franja":
                    # Asumimos que el bloqueo de franja también dura 2 horas por defecto
                    # O si el bloqueo tiene hora_fin, usarla.
                    # Por simplicidad, si hay un bloqueo que empieza en X, bloquea esa franja específica
                    # Pero para ser robustos, deberíamos chequear solapamiento si el bloqueo define rango.
                    # El modelo actual de bloqueo parece simple (hora_inicio).
                    # Asumiremos que un bloqueo en "10:00" bloquea 10-12.
                    b_fin = f"{int(b.hora_inicio.split(':')[0]) + 2}:00"
                    if hay_solapamiento(inicio, fin, b.hora_inicio, b_fin):
                        estado = "bloqueado"
                        break

        # Revisar si está reservado (solapamiento)
        if estado != "bloqueado":
            for r in reservas:
                if hay_solapamiento(inicio, fin, r.hora_inicio, r.hora_fin):
                    estado = "reservado"
                    break

        respuesta.append({
            "inicio": inicio,
            "fin": fin,
            "estado": estado
        })

    return respuesta
