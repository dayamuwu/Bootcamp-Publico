from dojos_app.config.mysqlconect import connectToMySQL


class Ninjas:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
    
    
    
    @classmethod
    def guardar_ninja(cls,data):
        query="INSERT INTO ninjas(nombre,apellido,edad,dojo_id) VALUES(%(nombre)s,%(apellido)s,%(edad)s,%(dojo_id)s);"
        return connectToMySQL('dojos_y_ninjas_02').query_db(query,data)




    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_y_ninjas_02').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos



    @classmethod
    def destroy_dojo(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_y_ninjas_02').query_db(query,data)