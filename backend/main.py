from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.database import Base, engine

# Modelos
from backend.models.user import Usuario
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo

# Routers
from backend.routers import auth, reservas, disponibilidad, admin

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reservas FISI - Web Backend",
    description="Sistema de reservas para la Facultad de Ingeniería de Sistemas",
    version="1.0.0"
)

# CORS mejorado
origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:3000",  # 👈 NUEVO: Para React/Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Manejo global de excepciones
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"}
    )

# Include routers
app.include_router(auth.router)
app.include_router(reservas.router)
app.include_router(disponibilidad.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"msg": "API Reservas FISI conectada a MySQL", "status": "active"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}