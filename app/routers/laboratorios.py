from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/laboratorios", tags=["laboratorios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.LaboratorioInDB)
def crear_laboratorio(l: schemas.LaboratorioCreate, db: Session = Depends(get_db)):
    return crud.create_laboratorio(db, l)

@router.get("/", response_model=list[schemas.LaboratorioInDB])
def listar_laboratorios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_laboratorios(db, skip, limit)

@router.get("/recientes", response_model=list[schemas.LaboratorioReciente])
def listar_laboratorios_recientes(db: Session = Depends(get_db)):
    return crud.get_laboratorios_recientes(db)

@router.get("/{lab_id}", response_model=schemas.LaboratorioInDB)
def obtener_laboratorio(lab_id: int, db: Session = Depends(get_db)):
    lab = crud.get_laboratorio(db, lab_id)
    if not lab:
        raise HTTPException(404, "Laboratorio no encontrado")
    return lab

@router.put("/{lab_id}", response_model=schemas.LaboratorioInDB)
def actualizar_laboratorio(lab_id: int, datos: schemas.LaboratorioUpdate, db: Session = Depends(get_db)):
    lab = crud.update_laboratorio(db, lab_id, datos)
    if not lab:
        raise HTTPException(404, "Laboratorio no encontrado")
    return lab

@router.delete("/{lab_id}", response_model=schemas.LaboratorioInDB)
def borrar_laboratorio(lab_id: int, db: Session = Depends(get_db)):
    lab = crud.delete_laboratorio(db, lab_id)
    if not lab:
        raise HTTPException(404, "Laboratorio no encontrado")
    return lab
