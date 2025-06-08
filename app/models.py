# app/models.py
from sqlalchemy import Column, String, Integer, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class SexoEnum(str, enum.Enum):
    M = "M"
    F = "F"

class Paciente(Base):
    __tablename__ = "pacientes"
    id               = Column(Integer, primary_key=True, index=True)
    nombre           = Column("nombre", String(128), nullable=False)
    apellido         = Column("apellido", String(128), nullable=False)
    fecha_nacimiento = Column("fecha_nacimiento", Date, nullable=False)
    sexo             = Column("sexo", Enum(SexoEnum), nullable=False)
    telefono         = Column("telefono", String(15), unique=True, nullable=False)
    correo           = Column("correo", String(255), unique=True, nullable=False)
    tipo_sangre      = Column("tipo_sangre", String, nullable=False)  # enum en BD

class Laboratorio(Base):
    __tablename__ = "laboratorios"
    id        = Column(Integer, primary_key=True, index=True)
    nombre    = Column("nombre", String(128), nullable=False)
    ubicacion = Column("ubicacion", String, nullable=False)

# ———— tus clases de VistaPacientesRecientes y VistaLaboratoriosRecientes siguen igual ————
