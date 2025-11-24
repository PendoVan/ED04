# backend/schema/bloqueo_schema.py
from pydantic import BaseModel, validator
from datetime import date, datetime
from typing import Optional, List

class BloqueoFranjaRequest(BaseModel):
    fecha: str
    hora_inicio: str

    @validator('hora_inicio')
    def validar_hora_inicio(cls, v):
        try:
            hora = int(v.split(':')[0])
            if hora < 10 or hora >= 18:
                raise ValueError('La hora debe estar entre 10:00 y 17:00')
            if not v.endswith(':00'):
                raise ValueError('El formato debe ser HH:00 (ej: 14:00)')
            return f"{hora:02d}:00"
        except (ValueError, IndexError):
            raise ValueError('Formato inválido. Use HH:00 (ej: 14:00)')

class BloqueoDiaRequest(BaseModel):
    fecha: str

    @validator('fecha')
    def validar_formato_fecha(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
            return v
        except ValueError:
            raise ValueError('Formato de fecha inválido. Use YYYY-MM-DD')

    @validator('fecha')
    def validar_fecha_futura(cls, v):
        fecha_obj = datetime.strptime(v, '%Y-%m-%d').date()
        hoy = date.today()
        if fecha_obj < hoy:
            raise ValueError('No se puede bloquear fechas pasadas')
        return v

class BloqueoResponse(BaseModel):
    id: int
    fecha: date
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    tipo: str

    class Config:
        orm_mode = True

class BloqueoListResponse(BaseModel):
    dia_bloqueado: bool
    bloqueos_franja: List[BloqueoResponse]

class BloqueoDeleteRequest(BaseModel):
    bloqueo_id: int

    @validator('bloqueo_id')
    def validar_id_positivo(cls, v):
        if v <= 0:
            raise ValueError('ID debe ser positivo')
        return v
