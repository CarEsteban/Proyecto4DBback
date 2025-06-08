from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Time,
    DateTime,
    Text,
    ForeignKey,
    Enum,
    DECIMAL
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Enums
sexo_enum = Enum('M', 'F', name='sexo_enum')
tipo_sangre_enum = Enum('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-', name='tipo_sangre_enum')
estado_cita_enum = Enum('programada', 'completada', 'cancelada', name='estado_cita_enum')

# Tablas principales
class Paciente(Base):
    __tablename__ = "pacientes"
    id               = Column(Integer, primary_key=True, index=True)
    nombre           = Column(String(128), nullable=False)
    apellido         = Column(String(128), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    sexo             = Column(sexo_enum, nullable=False)
    telefono         = Column(String(15), nullable=False, unique=True)
    correo           = Column(String(255), nullable=False, unique=True)
    tipo_sangre      = Column(tipo_sangre_enum, nullable=False)

class Medico(Base):
    __tablename__ = "medicos"
    id               = Column(Integer, primary_key=True, index=True)
    nombre           = Column(String(128), nullable=False)
    apellido         = Column(String(128), nullable=False)
    telefono         = Column(String(15), nullable=False, unique=True)
    correo           = Column(String(255), nullable=False, unique=True)
    fecha_nacimiento = Column(Date, nullable=False)

class Especialidad(Base):
    __tablename__ = "especialidades"
    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(255), nullable=False, unique=True)
    descripcion = Column(Text, nullable=False)

class MedicoEspecialidad(Base):
    __tablename__ = "medico_especialidad"
    id              = Column(Integer, primary_key=True, index=True)
    id_medico       = Column(Integer, ForeignKey("medicos.id"), nullable=False)
    id_especialidad = Column(Integer, ForeignKey("especialidades.id"), nullable=False)

    medico      = relationship("Medico", backref="especialidades_asignadas")
    especialidad= relationship("Especialidad", backref="medicos")

# Citas y hospitalizaciones
table_citas = "citas"
class Cita(Base):
    __tablename__ = table_citas
    id          = Column(Integer, primary_key=True, index=True)
    id_paciente = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_medico   = Column(Integer, ForeignKey("medicos.id"), nullable=True)
    fecha       = Column(Date, nullable=False)
    hora        = Column(Time, nullable=False)
    motivo      = Column(Text)
    estado      = Column(estado_cita_enum)

class Habitacion(Base):
    __tablename__ = "habitaciones"
    id     = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, nullable=False)
    piso   = Column(Integer, nullable=False)

class Hospitalizacion(Base):
    __tablename__ = "hospitalizaciones"
    id            = Column(Integer, primary_key=True, index=True)
    id_paciente   = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_habitacion = Column(Integer, ForeignKey("habitaciones.id"), nullable=True)
    fecha_ingreso = Column(Date, nullable=False)
    fecha_egreso  = Column(Date)
    motivo        = Column(Text, nullable=False)

# Recetas y medicamentos
class Receta(Base):
    __tablename__ = "recetas"
    id          = Column(Integer, primary_key=True, index=True)
    id_paciente = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_medico   = Column(Integer, ForeignKey("medicos.id"), nullable=False)
    fecha       = Column(Date, nullable=False)

class Medicamento(Base):
    __tablename__ = "medicamentos"
    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String, nullable=False)
    descripcion = Column(Text, nullable=False)
    stock       = Column(Integer, nullable=False)

class DetalleReceta(Base):
    __tablename__ = "detalle_receta"
    id             = Column(Integer, primary_key=True, index=True)
    id_receta      = Column(Integer, ForeignKey("recetas.id"), nullable=False)
    id_medicamento = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    cantidad       = Column(Integer, nullable=False)
    dosis          = Column(String(128), nullable=False)
    frecuencia     = Column(String(50), nullable=False)
    duracion       = Column(String(50), nullable=False)

# Diagnósticos y tratamientos
class Diagnostico(Base):
    __tablename__ = "diagnosticos"
    id           = Column(Integer, primary_key=True, index=True)
    id_paciente  = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_medico    = Column(Integer, ForeignKey("medicos.id"), nullable=False)
    fecha        = Column(Date, nullable=False)
    descripcion  = Column(Text)
    observaciones= Column(Text)

class Tratamiento(Base):
    __tablename__ = "tratamientos"
    id            = Column(Integer, primary_key=True, index=True)
    id_diagnostico= Column(Integer, ForeignKey("diagnosticos.id"), nullable=False)
    nombre        = Column(String(128), nullable=False)
    descripcion   = Column(Text, nullable=False)
    duracion      = Column(Time, nullable=False)

# Laboratorios y exámenes
class Examen(Base):
    __tablename__ = "examenes"
    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    tipo        = Column(String, nullable=False)

class Laboratorio(Base):
    __tablename__ = "laboratorios"
    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(128), nullable=False)
    ubicacion   = Column(Text, nullable=False)
    fecha       = Column(Date)
    resultado   = Column(String(255))
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medico_id   = Column(Integer, ForeignKey("medicos.id"))  # <-- AGREGA ESTA LÍNEA

    paciente = relationship("Paciente", backref="laboratorios")
    medico   = relationship("Medico", backref="laboratorios")

class LaboratorioExamen(Base):
    __tablename__ = "laboratorio_examen"
    id             = Column(Integer, primary_key=True, index=True)
    id_laboratorio = Column(Integer, ForeignKey("laboratorios.id"), nullable=False)
    id_examen      = Column(Integer, ForeignKey("examenes.id"), nullable=False)
    precio         = Column(DECIMAL(10, 2), nullable=False)

class ResultadoExamen(Base):
    __tablename__ = "resultado_examenes"
    id           = Column(Integer, primary_key=True, index=True)
    id_paciente  = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    id_examen    = Column(Integer, ForeignKey("examenes.id"), nullable=False)
    resultado    = Column(String(255), nullable=False)
    observaciones= Column(Text)
    created_at   = Column(DateTime, nullable=False)

# Vistas de solo lectura
class VistaPacientesRecientes(Base):
    __tablename__ = "vista_pacientes_recientes"
    name        = Column(String, primary_key=True)
    lastname    = Column(String, primary_key=True)
    birthdate   = Column(Date)
    sex         = Column(String)
    lastupdate  = Column(Date)
    manido      = Column(Integer)
    labname     = Column(String)

class VistaLaboratoriosRecientes(Base):
    __tablename__ = "vista_laboratorios_recientes"
    name         = Column(String, primary_key=True)
    lastname     = Column(String, primary_key=True)
    result       = Column(String)
    resultupdate = Column(Date)
    lastvisit    = Column(Date)
