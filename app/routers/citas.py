# app/routers/citas.py
from fastapi import APIRouter, Depends
from datetime import date
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/citas", tags=["citas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.CitaInDB)
def crear_cita(in_: schemas.CitaCreate, db: Session = Depends(get_db)):
    return crud.create_cita(db, in_)

@router.get("/", response_model=list[schemas.CitaInDB])
def listar_citas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_citas(db, skip, limit)

@router.get("/fecha/{fecha}", response_model=list[schemas.CitaInDB])
def citas_por_fecha(fecha: date, db: Session = Depends(get_db)):
    return crud.get_citas_por_fecha(db, fecha)

@router.put("/{id}", response_model=schemas.CitaInDB)
def actualizar_cita(id: int, datos: schemas.CitaCreate, db: Session = Depends(get_db)):
    return crud.update_cita(db, id, datos)

@router.delete("/{id}", response_model=schemas.CitaInDB)
def borrar_cita(id: int, db: Session = Depends(get_db)):
    return crud.delete_cita(db, id)
