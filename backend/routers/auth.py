from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.user import Usuario
from backend.schema.user_schema import RegisterRequest, LoginRequest, LoginResponse

router = APIRouter(prefix="/auth", tags=["Autenticación"])

# Credenciales fijas del admin
ADMIN_CORREO = "adminfisi@unmsm.edu.pe"
ADMIN_PASSWORD = "FISI2024"


# ---------------------------
# REGISTRO DE ESTUDIANTE
# ---------------------------
@router.post("/registro")
def registro_usuario(data: RegisterRequest, db: Session = Depends(get_db)):
    correo = data.correo.lower()

    if not correo.endswith("@unmsm.edu.pe"):
        raise HTTPException(400, "El correo debe ser institucional (@unmsm.edu.pe).")

    existente = db.query(Usuario).filter(Usuario.correo == correo).first()
    if existente:
        raise HTTPException(400, "Este correo ya está registrado.")

    nuevo = Usuario(
        correo=correo,
        password_hash=data.password,  # texto plano solo para prototipo
        rol="student"
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return {
        "msg": "Usuario registrado correctamente",
        "id": nuevo.id,
        "correo": nuevo.correo,
        "rol": nuevo.rol,
    }


# ---------------------------
# LOGIN (ADMIN + ESTUDIANTE)
# ---------------------------
@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    correo = data.correo.lower()

    # ADMIN
    if correo == ADMIN_CORREO:
        if data.password != ADMIN_PASSWORD:
            raise HTTPException(400, "Contraseña incorrecta para administrador.")

        admin = db.query(Usuario).filter(Usuario.correo == correo).first()
        if not admin:
            admin = Usuario(
                correo=correo,
                password_hash=ADMIN_PASSWORD,
                rol="admin"
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)

        return LoginResponse(id=admin.id, correo=admin.correo, rol=admin.rol)

    # ESTUDIANTE
    if not correo.endswith("@unmsm.edu.pe"):
        raise HTTPException(400, "El correo debe ser institucional.")

    user = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not user:
        raise HTTPException(400, "Usuario no registrado. Primero debe registrarse.")

    if data.password != user.password_hash:
        raise HTTPException(400, "Contraseña incorrecta.")

    return LoginResponse(id=user.id, correo=user.correo, rol=user.rol)
