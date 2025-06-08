# app/routers/resultado_examenes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/resultados", tags=["resultados"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ResultadoInDB)
def crear_resultado(in_: schemas.ResultadoCreate, db: Session = Depends(get_db)):
    return crud.create_resultado(db, in_)

@router.get("/", response_model=list[schemas.ResultadoInDB])
def listar_resultados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_resultados(db, skip, limit)

@router.get("/{id}", response_model=schemas.ResultadoInDB)
def obtener_resultado(id: int, db: Session = Depends(get_db)):
    return crud.get_resultado(db, id)

@router.put("/{id}", response_model=schemas.ResultadoInDB)
def actualizar_resultado(id: int, datos: schemas.ResultadoCreate, db: Session = Depends(get_db)):
    return crud.update_resultado(db, id, datos)

@router.delete("/{id}", response_model=schemas.ResultadoInDB)
def borrar_resultado(id: int, db: Session = Depends(get_db)):
    return crud.delete_resultado(db, id)
