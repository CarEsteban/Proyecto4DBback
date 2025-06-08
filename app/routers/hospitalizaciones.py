# app/routers/hospitalizaciones.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/hospitalizaciones", tags=["hospitalizaciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.HospInDB)
def crear_hosp(in_: schemas.HospCreate, db: Session = Depends(get_db)):
    return crud.create_hospitalizacion(db, in_)

@router.get("/", response_model=list[schemas.HospInDB])
def listar_hosp(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_hospitalizaciones(db, skip, limit)

@router.get("/actuales", response_model=list[schemas.HospInDB])
def hosp_actuales(db: Session = Depends(get_db)):
    return crud.get_hosp_actuales(db)

@router.get("/pasadas", response_model=list[schemas.HospInDB])
def hosp_pasadas(db: Session = Depends(get_db)):
    return crud.get_hosp_pasadas(db)

@router.put("/{id}", response_model=schemas.HospInDB)
def actualizar_hosp(id: int, datos: schemas.HospCreate, db: Session = Depends(get_db)):
    return crud.update_hospitalizacion(db, id, datos)

@router.delete("/{id}", response_model=schemas.HospInDB)
def borrar_hosp(id: int, db: Session = Depends(get_db)):
    return crud.delete_hospitalizacion(db, id)
