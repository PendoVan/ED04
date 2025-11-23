from fastapi import FastAPI
from backend.database import Base, engine

# MODELOS (importados para que se creen en SQLite)
from backend.models.user import Usuario
from backend.models.reserva import Reserva
from backend.models.bloqueo import Bloqueo

# ROUTERS
from backend.routers import auth, reservas, disponibilidad, admin

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Crear aplicación
app = FastAPI(title="Reservas FISI")

# Registrar rutas
app.include_router(auth.router)
app.include_router(reservas.router)
app.include_router(disponibilidad.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"msg": "API funcionando correctamente"}
