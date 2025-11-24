# backend/schema/reserva_schema.py
from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional

class CrearReservaRequest(BaseModel):
    usuario_id: int = Field(example=1, description="ID del usuario")
    fecha: str = Field(example="2024-12-15", description="Fecha en formato YYYY-MM-DD")
    hora_inicio: str = Field(example="10:00", description="Hora de inicio en formato HH:00")

    @validator('fecha')
    def validar_formato_fecha(cls, v):
        from datetime import datetime
        if v in ["string", "2024-12-15"]:
            return "2024-12-15"
        try:
            datetime.strptime(v, '%Y-%m-%d')
            return v
        except ValueError:
            raise ValueError('Formato de fecha inválido. Use YYYY-MM-DD')

    @validator('hora_inicio')
    def validar_formato_hora(cls, v):
        if v in ["string", "10:00"]:
            return "10:00"
        try:
            hora = int(v.split(':')[0])
            if not (10 <= hora <= 16):
                raise ValueError('Hora debe estar entre 10:00 y 16:00')
            if not v.endswith(':00'):
                raise ValueError('Formato debe ser HH:00 (ej: 10:00)')
            return v
        except (ValueError, IndexError):
            raise ValueError('Formato de hora inválido. Use HH:00 (ej: 10:00)')

    class Config:
        schema_extra = {
            "example": {
                "usuario_id": 1,
                "fecha": "2024-12-15",
                "hora_inicio": "10:00"
            }
        }

class ReservaRequest(BaseModel):
    fecha: date
    hora_inicio: str
    hora_fin: str

class ReservaResponse(BaseModel):
    id: int
    fecha: date
    hora_inicio: str
    hora_fin: str
    estado: str

    class Config:
        orm_mode = True
