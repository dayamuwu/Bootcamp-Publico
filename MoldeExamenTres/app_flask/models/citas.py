from datetime import datetime
from app_flask.models.usuarios import Usuarios
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash

class Citas:
    def __init__( self , data ):
        self.id = data['id']
        self.tareas = data['tareas']
        self.fecha = data['fecha']
        self.estado = data['estado']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
        self.sobre_usuarios=[]
        self.una_cita=[]



    @classmethod
    def guardar_cita(cls,data):
        query="INSERT INTO citas(tareas,fecha,estado, usuarios_id) VALUES(%(tareas)s,%(fecha)s,%(estado)s,%(usuario_id)s);"
        return connectToMySQL('citas_db').query_db(query,data)


    @classmethod
    def borrar_cita(cls,data):
        query = "DELETE FROM citas WHERE id = %(id)s;"
        return connectToMySQL('citas_db').query_db(query,data)

    @classmethod
    def get_all_citas(cls):
        query = "SELECT * FROM citas;"
        results = connectToMySQL('citas_db').query_db(query)
        citas = []
        for cit in results:
            citas.append( cls(cit) )
        return citas

    @classmethod
    def get_una_cita(cls,data):
        query = "SELECT * FROM citas WHERE id=%(id)s;"
        results = connectToMySQL('citas_db').query_db(query,data)
        return cls(results[0])


    @classmethod
    def update(cls,data):
        query = "UPDATE citas SET tareas=%(tareas)s, fecha=%(fecha)s, estado=%(estado)s WHERE id=%(id)s;"
        return connectToMySQL('citas_db').query_db(query,data)





    @staticmethod
    def validar_cita(registro):
        is_valid = True 
        if len(registro['tareas']) < 3:
            flash("Tareas debe contener al menos 3 caracteres")
            is_valid = False
    
        if datetime.strptime(registro['fecha']) < datetime.today():
            flash("Tareas debe contener al menos 3 caracteres")
            is_valid = False
        return is_valid