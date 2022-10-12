import re 
from examen_app.config.mysql import connectToMySQL
from flask import flash
EMAIL_REGEX=re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")


class Usuarios:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data ['nombre']
        self.apellido = data ['apellido']
        self.correo = data ['correo']
        self.contrasena = data ['contraseña']
        self.created_at = data ['created_at']
        self.update_at = data ['update_at']


    @classmethod
    def guardar_usuario(cls,data):
        query="INSERT INTO usuarios(nombre,apellido,correo,contraseña) VALUES(%(nombre)s,%(apellido)s,%(correo)s,%(contrasena)s);"
        return connectToMySQL('Tv_db').query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('Tv_db').query_db(query)
        usuarios = []
        for usu in results:
            usuarios.appen( cls(usu))
        return usuarios


    @classmethod
    def get_un_usuario(cls,data):
        query = "SELECT * FROM usuarios WHERE id=%(id)s;"
        results = connectToMySQL('Tv_db').query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_by_correo(cls,data):
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s;"
        result = connectToMySQL('Tv_db').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def destruir_usuario(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('Tv_db').query_db(query,data)


    @staticmethod
    def validar_usuario(registro):
        correo={
            "correo":registro['correo']
        }
        is_valid = True 
        if len(registro['nombre']) < 3:
            flash("Nombre debe contener al menos 3 caracteres")
            is_valid = False
        if len(registro['apellido']) < 3:
            flash("Apellido debe contener al menos 3 caracteres")
            is_valid = False
        if len(registro['contrasena']) < 2:
            flash("contrasena debe tener al menos 2 caracteres")
            is_valid = False
        if not EMAIL_REGEX.match(correo['correo']):
            flash("Correo no valido")
            is_valid = False
        elif Usuarios.get_by_correo(correo):
            flash("Correo ya existente")
            is_valid = False
        if registro['contrasena']!= registro['confcontrasena']:
            flash('contrasenas no coinciden')
            is_valid = False
        espacio=False
        mayus=False
        minus=False
        numeros=False
        for contr in registro['contrasena']:
            if contr.isspace()==True:
                espacio=True
            if contr.isdigit()==True:
                numeros=True
            if contr.islower()== True:
                minus=True
            if contr.isupper()== True:
                mayus=True
        if espacio==True:
            flash("contrasena no debe tener espacios en blanco")
            is_valid = False
        if mayus==False:
            flash("contrasena deben contener al menos una mayuscula")
            is_valid = False
        if numeros==False:
            flash("contrasena deben contener al menos un numero")
            is_valid = False
        if minus==False:
            flash("contrasena deben contener al menos una minuscula")
            is_valid = False
        return is_valid