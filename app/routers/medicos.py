# app/routers/medicos.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/medicos", tags=["medicos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MedicoInDB)
def crear_medico(in_: schemas.MedicoCreate, db: Session = Depends(get_db)):
    return crud.create_medico(db, in_)

@router.get("/", response_model=list[schemas.MedicoInDB])
def listar_medicos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_medicos(db, skip, limit)

@router.get("/{id}", response_model=schemas.MedicoInDB)
def obtener_medico(id: int, db: Session = Depends(get_db)):
    return crud.get_medico(db, id)

@router.get("/especialidad/{esp_id}", response_model=list[schemas.MedicoInDB])
def medicos_por_especialidad(esp_id: int, db: Session = Depends(get_db)):
    return crud.get_medicos_por_especialidad(db, esp_id)

@router.put("/{id}", response_model=schemas.MedicoInDB)
def actualizar_medico(id: int, datos: schemas.MedicoCreate, db: Session = Depends(get_db)):
    return crud.update_medico(db, id, datos)

@router.delete("/{id}", response_model=schemas.MedicoInDB)
def borrar_medico(id: int, db: Session = Depends(get_db)):
    return crud.delete_medico(db, id)
