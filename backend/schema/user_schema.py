# backend/schema/user_schema.py
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str

    @validator('correo')
    def correo_must_be_unmsm(cls, v):
        if v in ["string", "user@example.com"]:
            return "ejemplo@unmsm.edu.pe"
        if not v.endswith('@unmsm.edu.pe'):
            raise ValueError('El correo debe ser institucional (@unmsm.edu.pe)')
        return v

class LoginResponse(BaseModel):
    id: int
    correo: str
    rol: str
    fecha_creacion: Optional[datetime] = None

    class Config:
        "from_attributes" == True
