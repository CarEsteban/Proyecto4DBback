# app/routers/especialidades.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/especialidades", tags=["especialidades"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.EspecialidadInDB)
def crear_esp(in_: schemas.EspecialidadCreate, db: Session = Depends(get_db)):
    return crud.create_especialidad(db, in_)

@router.get("/", response_model=list[schemas.EspecialidadInDB])
def listar_esp(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_especialidades(db, skip, limit)

@router.get("/{id}", response_model=schemas.EspecialidadInDB)
def obtener_esp(id: int, db: Session = Depends(get_db)):
    return crud.get_especialidad(db, id)

@router.put("/{id}", response_model=schemas.EspecialidadInDB)
def actualizar_esp(id: int, datos: schemas.EspecialidadCreate, db: Session = Depends(get_db)):
    return crud.update_especialidad(db, id, datos)

@router.delete("/{id}", response_model=schemas.EspecialidadInDB)
def borrar_esp(id: int, db: Session = Depends(get_db)):
    return crud.delete_especialidad(db, id)
