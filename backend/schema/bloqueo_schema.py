# bloqueo schema
from pydantic import BaseModel, validator
from datetime import date
from typing import Optional

class BloqueoFranjaRequest(BaseModel):
    """Schema para crear un bloqueo de franja horaria (1 hora)"""
    fecha: str  # formato "YYYY-MM-DD"
    hora_inicio: str  # formato "HH:00"

    @validator('hora_inicio')
    def validar_hora_inicio(cls, v):
        try:
            hora = int(v.split(':')[0])
            if hora < 10 or hora >= 18:
                raise ValueError('La hora debe estar entre 10:00 y 17:00')
            if not v.endswith(':00'):
                raise ValueError('El formato debe ser HH:00 (ej: 14:00)')
            return f"{hora:02d}:00"  # 👈 Asegura formato consistente
        except (ValueError, IndexError):
            raise ValueError('Formato inválido. Use HH:00 (ej: 14:00)')

class BloqueoDiaRequest(BaseModel):
    """Schema para crear un bloqueo de día completo"""
    fecha: str  # formato "YYYY-MM-DD"

    @validator('fecha')
    def validar_fecha(cls, v):
        """Valida que la fecha esté en formato correcto"""
        from datetime import datetime
        try:
            datetime.strptime(v, '%Y-%m-%d')
            return v
        except ValueError:
            raise ValueError('Formato de fecha inválido. Use YYYY-MM-DD')
        
    from datetime import datetime, date

    @validator('fecha')
    def validar_fecha_futura(cls, v):
        """Valida que la fecha no sea en el pasado"""
        from datetime import datetime
        fecha_obj = datetime.strptime(v, '%Y-%m-%d').date()
        hoy = date.today()
        
        if fecha_obj < hoy:
            raise ValueError('No se puede bloquear fechas pasadas')
        
        return v

class BloqueoResponse(BaseModel):
    """Schema para la respuesta de un bloqueo"""
    id: int
    fecha: date
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    tipo: str  # "dia" o "franja"

    class Config:
        from_attributes = True

class BloqueoListResponse(BaseModel):
    """Schema para listar todos los bloqueos de una fecha"""
    dia_bloqueado: bool
    bloqueos_franja: list[BloqueoResponse]

class BloqueoDeleteRequest(BaseModel):
    """Schema para eliminar un bloqueo"""
    bloqueo_id: int

    @validator('bloqueo_id')
    def validar_id_positivo(cls, v):
        if v <= 0:
            raise ValueError('ID debe ser positivo')
        return v    