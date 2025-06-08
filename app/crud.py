# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

### PACIENTES CRUD ###
def get_paciente(db: Session, paciente_id: int):
    return db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, p: schemas.PacienteCreate):
    nuevo = models.Paciente(**p.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_paciente(db: Session, paciente_id: int, datos: schemas.PacienteUpdate):
    pac = get_paciente(db, paciente_id)
    if not pac:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(pac, field, val)
    db.commit()
    db.refresh(pac)
    return pac

def delete_paciente(db: Session, paciente_id: int):
    pac = get_paciente(db, paciente_id)
    if not pac:
        return None
    db.delete(pac)
    db.commit()
    return pac

### LABORATORIOS CRUD ###
def get_laboratorio(db: Session, lab_id: int):
    return db.query(models.Laboratorio).filter(models.Laboratorio.id == lab_id).first()

def get_laboratorios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Laboratorio).offset(skip).limit(limit).all()

def create_laboratorio(db: Session, l: schemas.LaboratorioCreate):
    nuevo = models.Laboratorio(**l.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_laboratorio(db: Session, lab_id: int, datos: schemas.LaboratorioUpdate):
    lab = get_laboratorio(db, lab_id)
    if not lab:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(lab, field, val)
    db.commit()
    db.refresh(lab)
    return lab

def delete_laboratorio(db: Session, lab_id: int):
    lab = get_laboratorio(db, lab_id)
    if not lab:
        return None
    db.delete(lab)
    db.commit()
    return lab

### VISTAS “RECIENTES” (solo lectura) ###
def get_pacientes_recientes(db: Session):
    return db.query(models.VistaPacientesRecientes).all()

def get_laboratorios_recientes(db: Session):
    return db.query(models.VistaLaboratoriosRecientes).all()
