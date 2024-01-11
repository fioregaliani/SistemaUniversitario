from modules.usuario import Usuario
from modules.reclamo import Reclamo
from modules.config import *

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()

        usuario1 = Usuario(
            email="federicogiussani.2001@gmail.com",
            contrasena="aucxxs125sd",
            nombre_usuario="Federico",
            apellido="Giussani",
            nombre="Federico",
            claustro="Estudiante"
        )
        db.session.add(usuario1)

        reclamo1 = Reclamo(
            id_usuario_creador=1,
            depto = "Secretaría Técnica",
            estado = 'pendiente',
            texto = 'No hay papel',
            id_usuarios_adheridos = '1,2,5'
        )
        db.session.add(reclamo1)

        db.session.commit()