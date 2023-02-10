import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fecha_de_suscripcion = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favoritos = relationship('Favoritos', backref='usuario', lazy=True)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    altura = Column(Integer, nullable=False)
    genero = Column(String(250), nullable=False)
    peso = Column(Integer, nullable=False)
    favoritos = relationship('Favoritos', backref='personajes', lazy=True)
    
class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    habitantes = Column(Integer, nullable=False)
    periodo_orbital = Column(Integer, nullable=False)
    diametro = Column(Integer, nullable=False)
    favoritos = relationship('Favoritos', backref='planetas', lazy=True) 

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
