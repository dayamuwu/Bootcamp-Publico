from dojos_app.config.mysqlconect import connectToMySQL
from dojos_app.models import ninjas

class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['creado_en']
        self.updated_at = data['actualizado_en']
        self.ninjas=[]


    @classmethod
    def guardar_dojo(cls,data):
        query="INSERT INTO dojos(nombre) VALUES(%(nombre)s);"
        return connectToMySQL('dojos_y_ninjas_02').query_db(query,data)


    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_y_ninjas_02').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos


    @classmethod
    def get_un_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        resultados = connectToMySQL('dojos_y_ninjas_02').query_db(query,data)
        return cls(resultados[0])


    @classmethod
    def destruir_dojo(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_y_ninjas_02').query_db(query,data)


    @classmethod
    def get_dojos_y_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_y_ninjas_02').query_db(query,data)
        dojo=[]
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["id"], 
                "nombre" : row_from_db["nombre"], 
                "apellido" : row_from_db["apellido"],
                "edad" : row_from_db["edad"],
                "creado_en" : row_from_db["creado_en"],
                "actualizado_en" : row_from_db["actualizado_en"]
            }
            dojo.append(ninjas.Ninjas(ninja_data))
        return dojo
