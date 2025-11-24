from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from backend.database import Base, engine
from backend.routers import auth, reservas, disponibilidad, admin

app = FastAPI(title="Reservas FISI")

# CORS PARA PERMITIR FRONTEND EN 5500
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Routers
app.include_router(auth.router)
app.include_router(reservas.router)
app.include_router(disponibilidad.router)
app.include_router(admin.router)

# Servir archivos estáticos
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/")
def root():
    return RedirectResponse(url="/login.html")
