from modules.config import db
from sqlalchemy import Column, Integer, String, ForeignKey
from flask_login import UserMixin

reclamos_usuarios = db.Table('reclamos_usuarios',
                            Column('usuarios_id', Integer, ForeignKey('usuarios.id')),
                            Column('reclamos_id', Integer, ForeignKey('reclamos.id')))


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    contrasena = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    nombre_usuario = Column(String(100), nullable=False, unique=True)
    claustro = Column(String(100), nullable=False)
    rol = Column(Integer(), nullable=False, default=0) #0: usuario final, 1: jefe dpto, 2: secretar
   
    #relación uno a muchos
    reclamos_creados = db.relationship('Reclamo', backref='usuario_creador', foreign_keys='Reclamo.id_usuario_creador')
    
    #relación muchos a muchos
    reclamos_adheridos = db.relationship('Reclamo', secondary=reclamos_usuarios, backref='adherentes')
    
    #relacion uno a muchos
    #reclamos_creados = db.relationship('Reclamo', backref='usuario_creador')

    #relacion muchos a muchos
    #reclamos_adheridos = db.relationship('Reclamo', secondary=reclamos_usuarios, backref='adherentes')


    