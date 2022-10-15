from primer_app import app
from flask import render_template, request, redirect
from primer_app.models.gente import Usuarios

@app.route('/')
def index():
    todos_usuarios = Usuarios.get_all()
    print(todos_usuarios)
    return render_template("index.html", todos_usuarios = todos_usuarios)  


@app.route('/crear', methods=['POST'])
def crear_usuario():
    data = {
    "nombre": request.form["nombre"],
    "apellido": request.form["apellido"],
    "correo":  request.form["correo"],
}
    usuarios_id = Usuarios.guardar(data)
    return redirect('/')


@app.route('/crear')
def usuarios():
    return render_template("crear.html")


@app.route('/resultado', methods=['GET'])
def rtd():
    nombre=['nombre']
    apellido=['apellido']
    correo=['correo']
    return render_template('resultado.html', nombre=nombre, apellido=apellido, correo=correo)


@app.route('/borrar/<int:id>')
def borrar(id):
    data = {
        'id':id,
    }
    Usuarios.destruir(data)
    return redirect('/')


@app.route('/mostrar/<int:id>')
def mostrar(id):
    data = {
        'id': id
    }
    return render_template("mostrar.html",usuario=Usuarios.get_un_usuario(data))

@app.route('/editar/<int:id>')
def mostrar_edicion(id):
    data = {
        'id' : id
    }
    return render_template("editar.html",usuario=Usuarios.get_un_usuario(data))

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    data = {
        'id' : id,
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "correo" : request.form["correo"]
    }
    Usuarios.update(data)
    return redirect(f"/mostrar/{id}")

