import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# URL a tu Postgres:
SQLALCHEMY_DATABASE_URL = "postgresql://escu:123456@localhost/proyecto4bd"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# Directorio donde están los .sql
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)
SQL_DIR = os.path.join(BASE_DIR, "bd")

def init_db():
    """
    Ejecuta en orden cada uno de los .sql dentro de bd/
    usando una transacción para que si falla uno, haga rollback.
    """
    for nombre in [
        "ddl.sql",
        "data.sql",
        "functions.sql",
        "triggers.sql",
        "views.sql",
    ]:
        ruta = os.path.join(SQL_DIR, nombre)
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"No existe el script SQL: {ruta}")
        print(f"▶ Ejecutando {ruta}")
        sql = open(ruta, encoding="utf-8").read()
        # engine.begin() abre una transacción; si falla, revierte todo.
        with engine.begin() as conn:
            conn.execute(text(sql))
    print("✔️ Base de datos inicializada correctamente")