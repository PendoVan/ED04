# backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.database import Base, engine
from backend.models.user import Usuario
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo
from backend.routers.auth import router as auth_router
from backend.routers.reservas import router as reservas_router
from backend.routers.disponibilidad import router as disponibilidad_router
from backend.routers.admin import router as admin_router

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reservas FISI - Web Backend",
    description="Sistema de reservas para la Facultad de Ingeniería de Sistemas",
    version="1.0.0"
)

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"}
    )

app.include_router(auth_router)
app.include_router(reservas_router)
app.include_router(disponibilidad_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"msg": "API Reservas FISI conectada a MySQL", "status": "active"}

@app.get("/health")
def health_check():
    # Intentar conectar brevemente para comprobar DB
    try:
        with engine.connect() as conn:
            pass
        db_status = "connected"
    except Exception:
        db_status = "disconnected"
    return {"status": "healthy", "database": db_status}
