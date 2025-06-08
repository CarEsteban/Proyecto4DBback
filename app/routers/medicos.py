# app/routers/medicos.py
from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, models
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

@router.post("/{medico_id}/especialidad/{esp_id}")
def asociar_medico_especialidad(medico_id: int, esp_id: int, db: Session = Depends(get_db)):
    medico = db.query(models.Medico).filter(models.Medico.id == medico_id).first()
    if not medico:
        raise HTTPException(404, "Médico no encontrado")
    especialidad = db.query(models.Especialidad).filter(models.Especialidad.id == esp_id).first()
    if not especialidad:
        raise HTTPException(404, "Especialidad no encontrada")
    existe = db.query(models.MedicoEspecialidad).filter_by(id_medico=medico_id, id_especialidad=esp_id).first()
    if existe:
        raise HTTPException(400, "Ya existe la relación")
    rel = models.MedicoEspecialidad(id_medico=medico_id, id_especialidad=esp_id)
    db.add(rel)
    db.commit()
    return {"ok": True}