from sqlalchemy import Column, Integer, String, Date
from backend.database import Base

class Bloqueo(Base):
    __tablename__ = "bloqueos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True)
    hora_inicio = Column(String, nullable=True)  # None → bloqueo de día completo
    hora_fin = Column(String, nullable=True)
    tipo = Column(String)  # "dia" o "franja"
