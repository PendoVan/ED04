from fastapi import FastAPI
from .database import Base, engine
from .routers import reservas

app = FastAPI(title="Sistema de Reservas FISI")

Base.metadata.create_all(bind=engine)

app.include_router(reservas.router)

@app.get("/")
def home():
    return {"mensaje": "API de Reservas FISI funcionando"}