from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Table, ARRAY
from flask_login import UserMixin
from datetime import datetime

class Reclamo(UserMixin, db.Model):
    __tablename__ = 'reclamos'
    #SQLAlchemy generará automáticamente un id único y lo asignará al objeto nuevo_reclamo 
    #cuando se realice la operación db.session.commit()
    id = Column(Integer(), primary_key=True)
    #relacion uno a muchos
    id_usuario_creador = Column(Integer(), ForeignKey('usuarios.id'), nullable=False)
    fecha_hora = Column(DateTime(), default=datetime.now())
    depto = Column(String(20), nullable=True) # derivar_reclamo cambia el dpto
    estado = Column(String(50), nullable=False, default="Pendiente")
    texto = Column(Text(), nullable=False)
    #imagen = Column(String(255))
    #adherentes = lista