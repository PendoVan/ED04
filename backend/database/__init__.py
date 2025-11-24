import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+mysqlconnector://root:admin123@localhost:3306/reservas_fisi"
)

# Opciones del engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
)

# Probar conexión al iniciar
try:
    with engine.connect() as conn:
        pass
except Exception as e:
    # Lanzar error claro para que se vea al iniciar la app
    raise RuntimeError(f"Error conectando a la base de datos: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
