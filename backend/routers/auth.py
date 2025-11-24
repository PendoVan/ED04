from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.user import Usuario
from backend.schema.user_schema import LoginRequest, LoginResponse

router = APIRouter(prefix="/auth", tags=["Autenticación"])

def validar_credenciales_institucion(correo: str, password: str) -> bool:
    """
    Valida credenciales contra sistema institucional
    """
    if not correo.endswith("@unmsm.edu.pe"):
        return False
    if not password or len(password.strip()) == 0:
        return False
    return True

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    correo = data.correo.lower().strip()
    
    # 1. LOGIN ADMIN
    if correo == "adminfisi@unmsm.edu.pe" and data.password == "FISI2024":
        admin = db.query(Usuario).filter(Usuario.correo == correo).first()
        if not admin:
            admin = Usuario(
                correo=correo, 
                password_hash="FISI2024", 
                rol="admin"
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
        return LoginResponse(id=admin.id, correo=admin.correo, rol="admin")

    # 2. LOGIN ESTUDIANTE
    if not validar_credenciales_institucion(correo, data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas o correo no institucional."
        )

    # Buscar o crear usuario
    user = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not user:
        user = Usuario(
            correo=correo,
            password_hash="EXTERNA",
            rol="student"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return LoginResponse(id=user.id, correo=user.correo, rol=user.rol)