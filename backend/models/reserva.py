from sqlalchemy import Column, Integer, String, Date, ForeignKey
from backend.database.database import Base
from sqlalchemy.orm import relationship

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha = Column(Date, index=True)
    hora_inicio = Column(String(10))
    hora_fin = Column(String(10))
    estado = Column(String(20), default="reservado")

    usuario = relationship("Usuario", back_populates="reservas")




