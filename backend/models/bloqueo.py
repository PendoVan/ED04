from sqlalchemy import Column, Integer, String, Date
from backend.database.database import Base

class Bloqueo(Base):
    __tablename__ = "bloqueos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)
    hora_inicio = Column(String(10), nullable=True)  # null para bloqueo de día completo
    hora_fin = Column(String(10), nullable=True)
    tipo = Column(String(10))  # "dia" o "franja"
