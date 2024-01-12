from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Table, ARRAY
from flask_login import UserMixin
from datetime import datetime
from modules.clasificador import Clasificador
import pickle


class Reclamo(UserMixin, db.Model):
    __tablename__ = 'reclamo'
    #SQLAlchemy generará automáticamente un id único y lo asignará al objeto nuevo_reclamo 
    #cuando se realice la operación db.session.commit()
    id = Column(Integer(), primary_key=True)
    id_usuario_creador = Column(Integer(), nullable=False) #id del usuario que lo creo
    fecha_hora = Column(DateTime(), default=datetime.now())
    texto = Column(Text(), nullable=False)
    depto = Column(String(20), nullable=False) # derivar_reclamo cambia el dpto
    estado = Column(String(50), nullable=False, default="Pendiente")
    id_usuarios_adheridos = Column(String(1000), nullable=True)

    def __init__(self, id_usuario_creador, texto):
        self.id_usuario_creador = id_usuario_creador
        self.texto = texto
        self.depto = self.clasificar_reclamo(texto)

    def clasificar_reclamo(self, descrip_reclamo):
        with open('./data/clasificador_svm.pkl', 'rb') as archivo:
            cls  = pickle.load(archivo)
            resultado = ''.join(cls.clasificar(descrip_reclamo))
            
        return resultado  #el metodo clasificar devuelve una lista con el valor de la clasificación