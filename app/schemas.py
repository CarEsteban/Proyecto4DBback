from pydantic import BaseModel, EmailStr
from datetime import date, datetime, time
from typing import Optional

# --------------------- Pacientes CRUD ---------------------
class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    sexo: str
    telefono: str
    correo: EmailStr
    tipo_sangre: str

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    sexo: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[EmailStr] = None
    tipo_sangre: Optional[str] = None

class PacienteInDB(PacienteBase):
    id: int
    class Config:
        from_attributes = True

# --------------------- Laboratorios CRUD ---------------------
class LaboratorioBase(BaseModel):
    nombre: str
    ubicacion: str
    paciente_id: int
    medico_id: int
    fecha: Optional[date] = None
    resultado: Optional[str] = None

class LaboratorioCreate(LaboratorioBase):
    pass

class LaboratorioUpdate(BaseModel):
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None

class LaboratorioInDB(LaboratorioBase):
    id: int
    class Config:
        from_attributes = True

# --------------------- Vistas "Recientes" ---------------------
class PacienteReciente(BaseModel):
    name: str
    lastname: str
    birthdate: date
    sex: str
    lastUpdate: Optional[datetime] = None
    manido: Optional[int] = None
    labname: str
    class Config:
        from_attributes = True

class LaboratorioReciente(BaseModel):
    paciente_nombre: str
    paciente_apellido: str
    laboratorio_nombre: str
    medico_nombre: str
    fecha: str
    resultado: str
    class Config:
        orm_mode = True

# --------------------- Laboratorio_Examen ---------------------
class LabExamenBase(BaseModel):
    id_laboratorio: int
    id_examen: int
    precio: float

class LabExamenCreate(LabExamenBase):
    pass

class LabExamenInDB(LabExamenBase):
    id: int
    class Config:
        from_attributes = True

# --------------------- Resultado_Examenes ---------------------
class ResultadoBase(BaseModel):
    id_paciente: int
    id_examen: int
    resultado: str
    observaciones: Optional[str] = None

class ResultadoCreate(ResultadoBase):
    pass

class ResultadoUpdate(BaseModel):
    resultado: Optional[str] = None
    observaciones: Optional[str] = None

class ResultadoInDB(ResultadoBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# --------------------- Citas ---------------------
class CitaBase(BaseModel):
    id_paciente: int
    id_medico: Optional[int] = None
    fecha: date
    hora: time
    motivo: Optional[str] = None
    estado: str

class CitaCreate(CitaBase):
    pass

class CitaUpdate(BaseModel):
    id_paciente: Optional[int] = None
    id_medico: Optional[int] = None
    fecha: Optional[date] = None
    hora: Optional[time] = None
    motivo: Optional[str] = None
    estado: Optional[str] = None

class CitaInDB(CitaBase):
    id: int
    class Config:
        from_attributes = True

# --------------------- Hospitalizaciones ---------------------
class HospBase(BaseModel):
    id_paciente: int
    id_habitacion: Optional[int] = None
    fecha_ingreso: date
    fecha_egreso: Optional[date] = None
    motivo: str

class HospCreate(HospBase):
    pass

class HospUpdate(BaseModel):
    id_paciente: Optional[int] = None
    id_habitacion: Optional[int] = None
    fecha_ingreso: Optional[date] = None
    fecha_egreso: Optional[date] = None
    motivo: Optional[str] = None

class HospInDB(HospBase):
    id: int
    class Config:
        from_attributes = True

# --------------------- Especialidades ---------------------
class EspecialidadBase(BaseModel):
    nombre: str
    descripcion: str

class EspecialidadCreate(EspecialidadBase):
    pass

class EspecialidadUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class EspecialidadInDB(EspecialidadBase):
    id: int
    class Config:
        from_attributes = True

# --------------------- Medicos ---------------------
class MedicoBase(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    correo: EmailStr
    fecha_nacimiento: date

class MedicoCreate(MedicoBase):
    pass

class MedicoUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[EmailStr] = None
    fecha_nacimiento: Optional[date] = None

class MedicoInDB(MedicoBase):
    id: int
    class Config:
        from_attributes = True
