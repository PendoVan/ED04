from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(100), nullable=False)
    rol = Column(String(20), nullable=False, default="student")
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())  # 👈 NUEVO

    reservas = relationship("Reserva", back_populates="usuario", cascade="all, delete-orphan")  # 👈 MEJORA