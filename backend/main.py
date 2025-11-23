from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import auth, reservas
from backend.routers import disponibilidad


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Reservas FISI")

app.include_router(auth.router)
app.include_router(reservas.router)
app.include_router(disponibilidad.router)


@app.get("/")
def root():
    return {"msg": "API funcionando correctamente"}

