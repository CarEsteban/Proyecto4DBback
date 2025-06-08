# app/models.py
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, DECIMAL, Enum, Time, Text
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
class LaboratorioExamen(Base):
    __tablename__ = "laboratorio_examen"
    id             = Column(Integer, primary_key=True, index=True)
    id_laboratorio = Column(Integer, ForeignKey("laboratorios.id"), nullable=False)
    id_examen      = Column(Integer, ForeignKey("examenes.id"), nullable=False)
    precio         = Column(DECIMAL(10,2), nullable=False)

class ResultadoExamen(Base):
    __tablename__ = "resultado_examenes"
    id           = Column(Integer, primary_key=True, index=True)
    id_paciente  = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_examen    = Column(Integer, ForeignKey("examenes.id"), nullable=False)
    resultado    = Column(String(255), nullable=False)
    observaciones= Column(Text)
    created_at   = Column(DateTime, nullable=False)

class Cita(Base):
    __tablename__ = "citas"
    id         = Column(Integer, primary_key=True, index=True)
    id_paciente= Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_medico  = Column(Integer, ForeignKey("medicos.id"))
    fecha      = Column(Date, nullable=False)
    hora       = Column(Time, nullable=False)
    motivo     = Column(Text)
    estado     = Column(Enum("programada","completada","cancelada", name="estado_cita_enum"))

class Hospitalizacion(Base):
    __tablename__ = "hospitalizaciones"
    id            = Column(Integer, primary_key=True, index=True)
    id_paciente   = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_habitacion = Column(Integer, ForeignKey("habitaciones.id"))
    fecha_ingreso = Column(Date, nullable=False)
    fecha_egreso  = Column(Date)
    motivo        = Column(Text, nullable=False)

class Especialidad(Base):
    __tablename__ = "especialidades"
    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(255), unique=True, nullable=False)
    descripcion = Column(Text, nullable=False)

class Medico(Base):
    __tablename__ = "medicos"
    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(128), nullable=False)
    apellido    = Column(String(128), nullable=False)
    telefono    = Column(String(15), unique=True, nullable=False)
    correo      = Column(String(255), unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)