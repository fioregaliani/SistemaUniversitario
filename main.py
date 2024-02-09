from modules.usuario import Usuario
from modules.reclamo import Reclamo
from modules.config import db, app
import pickle
from modules.clasificador import Clasificador
from modules.preprocesamiento import TextVectorizer

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
        
        #añadir usuarios y reclamos
        '''usuario1 = Usuario(
            email="federico.2000@gmail.com",
            contrasena="aucxxs125sd",
            nombre_usuario="Fede2000",
            apellido="Giussani",
            nombre="Federico",
            claustro="Estudiante"
        )
        db.session.add(usuario1)
        
        reclamo1 = Reclamo(
            id_usuario_creador=1,
            texto = "No funciona el campus de programacion avanzada."
        )
        db.session.add(reclamo1)
        db.session.commit()'''

        #aderir un usuario a un reclamo
        #usuario = db.session.get (Usuario, 2) #se busca el usuario
        #usuario1 = Usuario.query.filter_by(nombre_usuario='Fede').first()
        #print(usuario1.id)
        #reclamo = db.session.get (Reclamo, 2) #se busca el reclamo
        #print(reclamo.cantidad_de_adherentes())
        #usuario.reclamos_adheridos.append(reclamo)
        db.session.commit()
        #eliminar un adherente
        #reclamo.adherentes.remove(usuario)
        db.session.commit()
        #eliminar un reclamo
        #reclamo = db.session.get (Reclamo, 2)
        #db.session.delete(reclamo)
        db.session.commit()

        text = ["Falta agua en el modulo 5."]
        with open('./data/clasificador_svm.pkl', 'rb') as archivo:
            cls = pickle.load(archivo)

        lista = cls.clasificar(text)
        print(lista[0])
        