from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

MYSQL_USER = "root"
MYSQL_PASSWORD = "AlessandroGF26"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "reservas_fisi"

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://root:AlessandroGF26@localhost:3306/reservas_fisi"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,   # ⬅️ ACTIVAR LOGS SQL EN LA CONSOLA
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

