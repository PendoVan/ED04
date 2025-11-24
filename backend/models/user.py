from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    rol = Column(String(20))


    reservas = relationship("Reserva", back_populates="usuario")



