from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/recientes", response_model=list[schemas.LaboratorioReciente])
def listar_laboratorios_recientes(db: Session = Depends(get_db)):
    return crud.get_laboratorios_recientes(db)
