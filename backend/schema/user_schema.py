from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str

class LoginResponse(BaseModel):
    id: int
    correo: str
    rol: str

    class Config:
        orm_mode = True
