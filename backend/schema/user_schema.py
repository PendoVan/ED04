from pydantic import BaseModel

class RegisterRequest(BaseModel):
    correo: str
    password: str

class LoginRequest(BaseModel):
    correo: str
    password: str

class LoginResponse(BaseModel):
    id: int
    correo: str
    rol: str

    class Config:
        from_attributes = True
