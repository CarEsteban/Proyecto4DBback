from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import (
    pacientes, laboratorios,
    laboratorio_examen, resultado_examenes,
    citas, hospitalizaciones,
    especialidades, medicos
)
from app.database import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # O especifica ["http://localhost:5174"] si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa la base de datos al arrancar el backend
init_db()

for r in [
    pacientes.router, laboratorios.router,
    laboratorio_examen.router, resultado_examenes.router,
    citas.router, hospitalizaciones.router,
    especialidades.router, medicos.router
]:
    app.include_router(r)
#