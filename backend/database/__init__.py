import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool  # 👈 NUEVO

# Cadena de conexión para MySQL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:admin123@localhost:3306/reservas_fisi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    poolclass=NullPool  # 👈 MEJORA: Evita problemas de conexión en desarrollo
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()