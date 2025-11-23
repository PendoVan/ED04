from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(Date, index=True)
    hora_inicio = Column(String, index=True)
    hora_fin = Column(String, index=True)
    estado = Column(String, default="reservado")

    usuario = relationship("Usuario", back_populates="reservas")



