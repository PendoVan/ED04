from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.user import Usuario
from backend.schema.user_schema import LoginRequest, LoginResponse

router = APIRouter(prefix="/auth", tags=["Autenticación"])

# DATOS DEL ADMIN
ADMIN_CORREO = "adminfisi@unmsm.edu.pe"
ADMIN_PASSWORD = "FISI2024"


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    correo = data.correo.lower()
    password = data.password

    # ------------------------------
    # LOGIN ADMINISTRADOR
    # ------------------------------
    if correo == ADMIN_CORREO:
        if password != ADMIN_PASSWORD:
            raise HTTPException(400, "Contraseña incorrecta para administrador.")

        admin = db.query(Usuario).filter(Usuario.correo == correo).first()

        if not admin:
            admin = Usuario(
                correo=correo,
                password_hash=password,  # SIN HASH
                rol="admin"
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)

        return LoginResponse(
            id=admin.id,
            correo=admin.correo,
            rol=admin.rol
        )

    # ------------------------------
    # LOGIN ESTUDIANTE
    # ------------------------------
    if not correo.endswith("@unmsm.edu.pe"):
        raise HTTPException(400, "El correo debe ser institucional.")

    user = db.query(Usuario).filter(Usuario.correo == correo).first()

    # SI NO EXISTE → REGISTRO AUTOMÁTICO
    if not user:
        # CONTRASEÑA FIJA SIMPLE
        provisional = "12345678"

        if password != provisional:
            raise HTTPException(400, "Contraseña incorrecta para registro provisional.")

        user = Usuario(
            correo=correo,
            password_hash=provisional,  # SIN HASH
            rol="student"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        return LoginResponse(
            id=user.id,
            correo=user.correo,
            rol=user.rol
        )

    # SI EXISTE → COMPARACIÓN DIRECTA
    if password != user.password_hash:
        raise HTTPException(400, "Contraseña incorrecta.")

    return LoginResponse(
        id=user.id,
        correo=user.correo,
        rol=user.rol
    )
