from fastapi import FastAPI
from app.routers import (
    pacientes, laboratorios,
    laboratorio_examen, resultado_examenes,
    citas, hospitalizaciones,
    especialidades, medicos
)

app = FastAPI()

for r in [
    pacientes.router, laboratorios.router,
    laboratorio_examen.router, resultado_examenes.router,
    citas.router, hospitalizaciones.router,
    especialidades.router, medicos.router
]:
    app.include_router(r)
# 