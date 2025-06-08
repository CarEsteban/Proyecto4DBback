from sqlalchemy.orm import Session
from . import models

def get_pacientes_recientes(db: Session):
    return db.query(models.VistaPacientesRecientes).all()

def get_laboratorios_recientes(db: Session):
    return db.query(models.VistaLaboratoriosRecientes).all()
