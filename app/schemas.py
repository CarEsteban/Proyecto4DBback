from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

# Esquemas para Pacientes CRUD
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
    nombre: Optional[str]
    apellido: Optional[str]
    fecha_nacimiento: Optional[date]
    sexo: Optional[str]
    telefono: Optional[str]
    correo: Optional[EmailStr]
    tipo_sangre: Optional[str]

class PacienteInDB(PacienteBase):
    id: int

    class Config:
        from_attributes = True


# Esquemas para Laboratorios CRUD
class LaboratorioBase(BaseModel):
    nombre: str
    ubicacion: str

class LaboratorioCreate(LaboratorioBase):
    pass

class LaboratorioUpdate(BaseModel):
    nombre: Optional[str]
    ubicacion: Optional[str]

class LaboratorioInDB(LaboratorioBase):
    id: int

    class Config:
        from_attributes = True


# Esquemas para Endpoints "Recientes"
class PacienteReciente(BaseModel):
    name: str
    lastname: str
    birthdate: date
    sex: str
    lastUpdate: Optional[date] = None
    manido: Optional[int]   = None
    labname: str

    class Config:
        from_attributes = True

class LaboratorioReciente(BaseModel):
    name: str
    lastname: str
    result: str
    resultUpdate: Optional[date] = None
    lastVisit: Optional[date]    = None

    class Config:
        from_attributes = True
