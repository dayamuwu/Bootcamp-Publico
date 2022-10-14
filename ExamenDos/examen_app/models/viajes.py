from examen_app.models.usuarios import Usuarios
from examen_app.config.mysql import connectToMySQL
from flask import flash

class Viajes:
    def __init__( self , data ):
        self.id = data['id']
        self.plan = data['plan']
        self.inicio_viaje = data['inicio_viaje']
        self.fin_viaje = data['fin viaje']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
        self.sobre_usuarios=[]
        self.un_viaje=[]

    @classmethod
    def guardar_viaje(cls,data):
        query="INSERT INTO viajes(plan,inicio_viaje,fin_viaje,descripcion,usuarios_id) VALUES(%(plan)s,%(inicio_viaje)s,%(fin_viaje)s,%(descripcion)s,%(usuario_id)s);"
        return connectToMySQL('usuarios_y_viajes_db').query_db(query,data)

    @classmethod
    def get_all_viajes(cls):
        query = "SELECT * FROM viajes;"
        results = connectToMySQL('usuarios_y_viajes_db').query_db(query)
        viajes = []
        for via in results:
            viajes.append( cls(via) )
        return viajes

    @classmethod
    def get_un_viaje(cls,data):
        query = "SELECT * FROM viajes WHERE id=%(id)s;"
        results = connectToMySQL('usuarios_y_viajes_db').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE viajes SET plan=%(plan)s, inicio_viaje=%(inicio_viaje)s, fin_viaje=%(fin_viaje)s, descripcion=%(descripcion)s, created_at=%(created_at)s, updated_at = NOW(), WHERE id = %(id)s;"
        return connectToMySQL('usuarios_y_viajes_db').query_db(query,data)

    @classmethod
    def destruir_viaje(cls,data):
        query = "DELETE FROM viajes WHERE id = %(id)s;"
        return connectToMySQL('usuarios_y_viajes_db').query_db(query,data)

    @classmethod
    def get_usuario_viaje(cls):
        query = "SELECT * FROM viajes as r JOIN usuarios as u ON r.usuarios_id = u.id;"
        results = connectToMySQL('usuarios_y_viajes_db').query_db(query)
        lista_usuario=[]
        for row_from_db in results:
            obj_viaje=cls(row_from_db)
            obj_viaje.sobre_usuarios.append(Usuarios(row_from_db))
            lista_usuario.append(obj_viaje)
        return lista_usuario

    @classmethod
    def get_usuario_un_viaje(cls,data):
        query = "SELECT * FROM viajes as r JOIN usuarios as u ON r.usuarios_id = u.id WHERE r.id=%(id)s;"
        results = connectToMySQL('usuarios_y_viajes_db').query_db(query,data)
        lista_un_viaje=[]
        for row_from_db in results:
            obj_unviaje=cls(row_from_db)
            obj_unviaje.un_viaje.append(Usuarios(row_from_db))
            lista_un_viaje.append(obj_unviaje)
        return lista_un_viaje

    @staticmethod
    def validar_viaje(registro):
        is_valid = True 
        if len(registro['plan']) < 3:
            flash("Plan debe contener al menos 3 caracteres")
            is_valid = False
        return is_valid