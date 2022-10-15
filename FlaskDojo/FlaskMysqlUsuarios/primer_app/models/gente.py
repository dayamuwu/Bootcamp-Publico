from primer_app.config.mysql import connectToMySQL


class Usuarios:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data ['nombre']
        self.apellido = data ['apellido']
        self.correo = data ['correo']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('gente_db').query_db(query)
        usuarios = []
        for usu in results:
            usuarios.append( cls(usu))
        return usuarios
    
    @classmethod
    def get_un_usuario(cls,data):
        query = "SELECT * FROM usuarios WHERE id=%(id)s;"
        results = connectToMySQL('gente_db').query_db(query,data)
        return cls(results[0])

    @classmethod
    def guardar(cls,data):
        query="INSERT INTO usuarios(nombre,apellido, correo) VALUES(%(nombre)s,%(apellido)s,%(correo)s);"
        return connectToMySQL('gente_db').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, correo=%(correo)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('gente_db').query_db(query,data)

    @classmethod
    def destruir(cls,data):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('gente_db').query_db(query,data)




