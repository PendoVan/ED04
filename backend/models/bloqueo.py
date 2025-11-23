from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from backend.database import Base

class Bloqueo(Base):
    __tablename__ = "bloqueos"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, index=True, nullable=False)
    hora_inicio = Column(String(10), default=None)  # 👈 MEJORA: más claro
    hora_fin = Column(String(10), default=None)
    tipo = Column(String(20), nullable=False)  # "dia" o "franja"
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())  # 👈 NUEVO