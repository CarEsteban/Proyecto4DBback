# app/models.py
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VistaPacientesRecientes(Base):
    __tablename__ = "vista_pacientes_recientes"
    # define un PK único (p.ej. name+lastname o una columna extra que la vista genere)
    name       = Column(String, primary_key=True)
    lastname   = Column(String, primary_key=True)
    birthdate  = Column(Date)
    sex        = Column(String)
    lastupdate = Column("lastupdate", Date)
    manido     = Column(Integer)
    labname    = Column(String)

class VistaLaboratoriosRecientes(Base):
    __tablename__ = "vista_laboratorios_recientes"
    name         = Column(String, primary_key=True)
    lastname     = Column(String, primary_key=True)
    result       = Column(String)
    resultupdate = Column("resultupdate", Date)
    lastvisit    = Column("lastvisit", Date)
