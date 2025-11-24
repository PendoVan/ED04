from pydantic import BaseModel
from datetime import date

class BloqueoCreate(BaseModel):
    fecha: date
    inicio: str
    fin: str
    motivo: str

class BloqueoResponse(BaseModel):
    id: int
    fecha: date
    inicio: str
    fin: str
    motivo: str

    class Config:
        from_attributes = True
