from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/pacientes", tags=["pacientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD sobre pacientes
@router.post("/", response_model=schemas.PacienteInDB)
def crear_paciente(p: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.create_paciente(db, p)

@router.get("/", response_model=list[schemas.PacienteInDB])
def listar_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_pacientes(db, skip, limit)

@router.get("/{paciente_id}", response_model=schemas.PacienteInDB)
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db)):
    pac = crud.get_paciente(db, paciente_id)
    if not pac:
        raise HTTPException(404, "Paciente no encontrado")
    return pac

@router.put("/{paciente_id}", response_model=schemas.PacienteInDB)
def actualizar_paciente(paciente_id: int, datos: schemas.PacienteUpdate, db: Session = Depends(get_db)):
    pac = crud.update_paciente(db, paciente_id, datos)
    if not pac:
        raise HTTPException(404, "Paciente no encontrado")
    return pac

@router.delete("/{paciente_id}", response_model=schemas.PacienteInDB)
def borrar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    pac = crud.delete_paciente(db, paciente_id)
    if not pac:
        raise HTTPException(404, "Paciente no encontrado")
    return pac

# Listar “Recientes” (solo lectura)
@router.get("/recientes", response_model=list[schemas.PacienteReciente])
def listar_pacientes_recientes(db: Session = Depends(get_db)):
    return crud.get_pacientes_recientes(db)
