# schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class PacienteReciente(BaseModel):
    name: str
    lastname: str
    birthdate: date
    sex: str
    lastUpdate: Optional[date]   = None
    manido:    Optional[int]     = None
    labname:   str

    class Config:
        from_attributes = True

class LaboratorioReciente(BaseModel):
    name:         str
    lastname:     str
    result:       str
    resultUpdate: Optional[date] = None
    lastVisit:    Optional[date] = None

    class Config:
        from_attributes = True
