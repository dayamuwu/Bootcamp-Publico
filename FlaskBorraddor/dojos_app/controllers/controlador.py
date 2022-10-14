from dojos_app import app
from flask import render_template, request, redirect
from dojos_app.models.dojos import Dojos
from dojos_app.models.ninjas import Ninjas


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojo():
    dojos = Dojos.get_all_dojos()
    return render_template()


@app.route('/crear_dojo', methods=["POST"])
def crear_usr():
    data = {
        "nombre": request.form["nombre"]
    }
    Dojos.guardar_dojo(data)
    return redirect('/')


@app.route('/ninja')
def ninja():
    dojos = Dojos.get_all_dojos()
    return render_template("crear_ninja.html", todos_dojos = dojos)

@app.route('/crear_ninja', methods=["POST"])
def crear_ninja():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "edad":request.form["edad"],
        "dojo_id":request.form["dojo_id"]
    }
    id=data["dojo_id"]
    Ninjas.guardar_ninja(data)
    return redirect(f"/mostrar_dojo/{id}")

@app.route('/mostrar_dojo/<int:id>')
def mostrar_dojo(id):
    data = {
        'id': id
    }
    un_dojo=Dojos.get_un_dojo(data)
    todos_ninjas=Dojos.get_dojos_y_ninjas(data)
    return render_template("mostrar_dojo.html",todos_ninjas=todos_ninjas,un_dojo=un_dojo)