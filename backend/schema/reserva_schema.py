from pydantic import BaseModel
from datetime import date

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
        from_attributes = True

