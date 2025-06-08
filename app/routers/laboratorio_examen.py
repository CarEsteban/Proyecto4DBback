# app/routers/laboratorio_examenes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/laboratorio_examenes", tags=["laboratorio_examenes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.LabExamenInDB)
def crear_lab_examen(in_: schemas.LabExamenCreate, db: Session = Depends(get_db)):
    return crud.create_lab_examen(db, in_)

@router.get("/", response_model=list[schemas.LabExamenInDB])
def listar_lab_examenes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_lab_examenes(db, skip, limit)

@router.get("/{id}", response_model=schemas.LabExamenInDB)
def obtener_lab_examen(id: int, db: Session = Depends(get_db)):
    return crud.get_lab_examen(db, id)

@router.put("/{id}", response_model=schemas.LabExamenInDB)
def actualizar_lab_examen(id: int, datos: schemas.LabExamenCreate, db: Session = Depends(get_db)):
    return crud.update_lab_examen(db, id, datos)

@router.delete("/{id}", response_model=schemas.LabExamenInDB)
def borrar_lab_examen(id: int, db: Session = Depends(get_db)):
    return crud.delete_lab_examen(db, id)
