from fastapi import FastAPI
from app.database import init_db
from app.routers import pacientes, laboratorios

app = FastAPI(title="ProyectoDB API")

@app.on_event("startup")
def on_startup():
    init_db()

# Monta tus routers:
app.include_router(pacientes.router)
app.include_router(laboratorios.router)
