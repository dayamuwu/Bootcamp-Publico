from examen_app.models.usuarios import Usuarios
from examen_app.config.mysql import connectToMySQL
from flask import flash

class Programas:
    def __init__( self , data ):
        self.id = data['id']
        self.titulo = data['titulo']
        self.canal = data['canal']
        self.lanzamiento = data['lanzamiento']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']
        self.usuarios_id = data['usuarios_id']
        self.sobre_usuarios=[]
        self.un_programa=[]

    @classmethod
    def guardar_programa(cls,data):
        query="INSERT INTO programas(titulo,canal,lanzamiento,descripcion,created_at,update_at,usuarios_id) VALUES(%(titulos)s,%(canal)s,%(lanzamiento)s,%(descripcion)s,%(created_at)s,%(update_at)s,%(usuarios_id)s);"
        return connectToMySQL('Tv').query_db(query,data)

    @classmethod
    def get_all_programas(cls):
        query = "SELECT * FROM programas;"
        results = connectToMySQL('Tv').query_db(query)
        programas = []
        for prg in results:
            programas.append( cls(prg) )
        return programas

    @classmethod
    def get_one_programa(cls,data):
        query = "SELECT * FROM programas WHERE id=%(id)s;"
        results = connectToMySQL('Tv').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE programas SET titulo=%(titulo)s, canal=%(canal)s, lanzamiento=%(lanzamiento)s, descripcion=%(descripcion)s, created_at=%(created_at)s, updated_at = NOW(), WHERE id = %(id)s;"
        return connectToMySQL('Tv').query_db(query,data)

    @classmethod
    def destruir_programa(cls,data):
        query = "DELETE FROM programas WHERE id = %(id)s;"
        return connectToMySQL('Tv').query_db(query,data)

    @classmethod
    def get_usuario_programa(cls):
        query = "SELECT * FROM programas as r JOIN usuarios as u ON r.usuario_id = u.id;"
        results = connectToMySQL('Tv').query_db(query)
        lista_usuario=[]
        for row_from_db in results:
            obj_programa=cls(row_from_db)
            obj_programa.on_users.append(Usuarios(row_from_db))
            lista_usuario.append(obj_programa)
        return lista_usuario

    @classmethod
    def get_usuario_un_programa(cls,data):
        query = "SELECT * FROM programas as r JOIN usuarios as u ON r.usuario_id = u.id WHERE r.id=%(id)s;"
        results = connectToMySQL('Tv').query_db(query,data)
        lista_un_programa=[]
        for row_from_db in results:
            obj_unprograma=cls(row_from_db)
            obj_unprograma.un_programa.append(Usuarios(row_from_db))
            lista_un_programa.append(obj_unprograma)
        return lista_un_programa

    @staticmethod
    def validar_programa(registro):
        is_valid = True # asumimos que esto es true
        if len(registro['titulo']) < 3:
            flash("Titulo debe contener al menos 3 caracteres")
            is_valid = False
        if len(registro['canal']) < 2:
            flash("Canal debe contener al menos 2 caracteres")
            is_valid = False
        if len(registro['lanzamiento']) < 3:
            flash("Lanzamiento debe tener al menos 3 caracteres")
            is_valid = False
        return is_valid