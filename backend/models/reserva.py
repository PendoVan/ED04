from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)  # 👈 MEJORA
    fecha = Column(Date, index=True, nullable=False)
    hora_inicio = Column(String(10), nullable=False)
    hora_fin = Column(String(10), nullable=False)
    estado = Column(String(20), default="reservado", nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())  # 👈 NUEVO

    usuario = relationship("Usuario", back_populates="reservas")