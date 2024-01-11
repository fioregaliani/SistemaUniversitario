from modules.config import db
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    contrasena = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    nombre_usuario = Column(String(100), nullable=False, unique=True)
    claustro = Column(String(100), nullable=False)
    id_reclamos_creados = Column(String(), nullable=True)
    id_reclamos_adheridos = Column(String(), nullable=True)


    