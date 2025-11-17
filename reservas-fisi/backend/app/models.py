from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, nullable=False)
    cancha = Column(String, nullable=False)
    fecha = Column(Date, nullable=False)
