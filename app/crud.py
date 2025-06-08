# app/crud.py
from datetime import date
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
    return db.query(
        models.Paciente.nombre.label("paciente_nombre"),
        models.Paciente.apellido.label("paciente_apellido"),
        models.Laboratorio.nombre.label("laboratorio_nombre"),
        models.Medico.nombre.label("medico_nombre"),
        models.Laboratorio.fecha,
        models.Laboratorio.resultado.label("resultado")
    ).join(models.Laboratorio, models.Laboratorio.paciente_id == models.Paciente.id
    ).join(models.Medico, models.Laboratorio.medico_id == models.Medico.id
    ).order_by(models.Laboratorio.fecha.desc()
    ).limit(10).all()


### LABORATORIO_EXAMEN CRUD ###
def get_lab_examen(db: Session, id: int):
    return db.query(models.LaboratorioExamen).filter(models.LaboratorioExamen.id == id).first()

def get_lab_examenes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LaboratorioExamen).offset(skip).limit(limit).all()

def create_lab_examen(db: Session, in_: schemas.LabExamenCreate):
    obj = models.LaboratorioExamen(**in_.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_lab_examen(db: Session, id: int, datos: schemas.LabExamenCreate):
    obj = get_lab_examen(db, id)
    if not obj:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(obj, field, val)
    db.commit()
    db.refresh(obj)
    return obj

def delete_lab_examen(db: Session, id: int):
    obj = get_lab_examen(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


### RESULTADO_EXAMENES CRUD ###
def get_resultado(db: Session, id: int):
    return db.query(models.ResultadoExamen).filter(models.ResultadoExamen.id == id).first()

def get_resultados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ResultadoExamen).offset(skip).limit(limit).all()

def create_resultado(db: Session, in_: schemas.ResultadoCreate):
    obj = models.ResultadoExamen(**in_.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_resultado(db: Session, id: int, datos: schemas.ResultadoCreate):
    obj = get_resultado(db, id)
    if not obj:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(obj, field, val)
    db.commit()
    db.refresh(obj)
    return obj

def delete_resultado(db: Session, id: int):
    obj = get_resultado(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


### CITAS CRUD ###
def get_cita(db: Session, id: int):
    return db.query(models.Cita).filter(models.Cita.id == id).first()

def get_citas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cita).offset(skip).limit(limit).all()

def get_citas_por_fecha(db: Session, fecha: date):
    return db.query(models.Cita).filter(models.Cita.fecha == fecha).all()

def create_cita(db: Session, in_: schemas.CitaCreate):
    obj = models.Cita(**in_.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_cita(db: Session, id: int, datos: schemas.CitaCreate):
    obj = get_cita(db, id)
    if not obj:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(obj, field, val)
    db.commit()
    db.refresh(obj)
    return obj

def delete_cita(db: Session, id: int):
    obj = get_cita(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


### HOSPITALIZACIONES CRUD ###
def get_hospitalizacion(db: Session, id: int):
    return db.query(models.Hospitalizacion).filter(models.Hospitalizacion.id == id).first()

def get_hospitalizaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hospitalizacion).offset(skip).limit(limit).all()

def get_hosp_actuales(db: Session):
    return db.query(models.Hospitalizacion).filter(models.Hospitalizacion.fecha_egreso == None).all()

def get_hosp_pasadas(db: Session):
    return db.query(models.Hospitalizacion).filter(models.Hospitalizacion.fecha_egreso != None).all()

def create_hospitalizacion(db: Session, in_: schemas.HospCreate):
    obj = models.Hospitalizacion(**in_.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_hospitalizacion(db: Session, id: int, datos: schemas.HospCreate):
    obj = get_hospitalizacion(db, id)
    if not obj:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(obj, field, val)
    db.commit()
    db.refresh(obj)
    return obj

def delete_hospitalizacion(db: Session, id: int):
    obj = get_hospitalizacion(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


### ESPECIALIDADES CRUD ###
def get_especialidad(db: Session, id: int):
    return db.query(models.Especialidad).filter(models.Especialidad.id == id).first()

def get_especialidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Especialidad).offset(skip).limit(limit).all()

def create_especialidad(db: Session, in_: schemas.EspecialidadCreate):
    obj = models.Especialidad(**in_.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_especialidad(db: Session, id: int, datos: schemas.EspecialidadCreate):
    obj = get_especialidad(db, id)
    if not obj:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(obj, field, val)
    db.commit()
    db.refresh(obj)
    return obj

def delete_especialidad(db: Session, id: int):
    obj = get_especialidad(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj


### MEDICOS CRUD ###
def get_medico(db: Session, id: int):
    return db.query(models.Medico).filter(models.Medico.id == id).first()

def get_medicos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medico).offset(skip).limit(limit).all()

def get_medicos_por_especialidad(db: Session, esp_id: int):
    return (
        db.query(models.Medico)
        .join(models.MedicoEspecialidad, models.MedicoEspecialidad.id_medico == models.Medico.id)
        .filter(models.MedicoEspecialidad.id_especialidad == esp_id)
        .all()
    )

def create_medico(db: Session, in_: schemas.MedicoCreate):
    obj = models.Medico(**in_.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_medico(db: Session, id: int, datos: schemas.MedicoCreate):
    obj = get_medico(db, id)
    if not obj:
        return None
    for field, val in datos.dict(exclude_unset=True).items():
        setattr(obj, field, val)
    db.commit()
    db.refresh(obj)
    return obj

def delete_medico(db: Session, id: int):
    obj = get_medico(db, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj

def get_medicos_por_especialidad(db: Session, esp_id: int):
    return (
        db.query(models.Medico)
          .join(
            models.MedicoEspecialidad,
            models.MedicoEspecialidad.id_medico == models.Medico.id
          )
          .filter(models.MedicoEspecialidad.id_especialidad == esp_id)
          .all()
    )
