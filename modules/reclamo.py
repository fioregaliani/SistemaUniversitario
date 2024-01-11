from modules.config import db
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from flask_login import UserMixin

class Reclamo(UserMixin, db.Model):
    id_reclamo = Column(Integer(), primary_key=True)
    id_usuario_creador = Column(Integer(), nullable=False) 
    fecha_hora = Column(DateTime(), default=datetime.now())
    depto = Column(String(50), nullable=False) #cambia el dpto derivar_reclamo
    estado = Column(String(50), nullable=False)
    texto = Column(Text(), nullable=False)
    id_usuarios_adheridos = Column(String(1000), nullable=True)