#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x [1][0] = 15
print (x)

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]["last_name"] = "Bryant"
print (estudiantes)

#En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes ['fútbol'][0] = "Andres"
print (directorio_deportes)

#Cambia el valor 20 en z a 30.
z = [ {'x': 10, 'y': 20} ]
z [0]['y'] = 30
print (z)

#Iterar a través de una lista de diccionarios

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def itera():    

    for i in range(len(estudiantes)):
        print(f"first_name - "+ estudiantes[i]["first_name"]+ ", last_name - "+estudiantes[i]["last_name"] )

itera()    

#Obtener valores de una lista de diccionarios

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def obt_valores():

    for i in range(len(estudiantes)):
        print(estudiantes[i]["first_name"])

    for i in range(len(estudiantes)):
        print(estudiantes[i]["last_name"])

obt_valores()

#Iterar a través de un diccionarios con valores de lista

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def diccionari():

    print(str(len(dojo['ubicaciones']))+ " UBICACIONES")

    for i in range(len(dojo['ubicaciones'])):
        print(dojo['ubicaciones'][i])


    print(str(len(dojo['instructores']))+ " INSTRUCTORES")

    for i in range(len(dojo['instructores'])):
        print(dojo['instructores'][i])

diccionari()    