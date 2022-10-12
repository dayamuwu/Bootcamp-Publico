from calendar import day_abbr
from datetime import date,datetime
from examen_app.models.programa import Programas
from examen_app import app
from flask import render_template, request, redirect, session, flash
from examen_app.models.usuarios import Usuarios
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
app.secret_key = 'ch3st34r@'

@app.route('/')
def inicio():
    if 'id_usuario' not in session:
        return render_template("index.html")

@app.route('/crear', methods=['POST'])
def crear():
    valor=request.form['formu']
    if valor == "usuarios":
        pw_hash = bcrypt.generate_password_hash(request.form['contrasena'])
        data = {
            "nombre": request.form['nombre'],
            "apellido": request.form['apellido'],
            "correo": request.form['correo'],
            "contrasena" : pw_hash
        }
        if not Usuarios.validar_usuario(request.form):
            return redirect("/")
        usuario_id = Usuarios.guardar_usuario(data)
        session['usuario_id'] = usuario_id
        flash("Usuario creado correctamente, ahora puedes logearte")
        return redirect('/')
    elif valor == "programas":
        data = {
            "titulo":request.form["titulo"],
            "canal":request.form["canal"],
            "lanzamiento":request.form["lanzamiento"],
            "descripcion":request.form["descripcion"],
            "usuario_id":session['usuario_id']
        }
        if not Programas.validar_programa(request.form):
            return redirect("/programa")
        Programas.guardar_programa(data)
        flash("Programa creado correctamente")
        return redirect('/programa')


@app.route('/login', methods=['POST'])
def login():
    data = {
        "correo" : request.form["correo"]
    }
    user_in_db = Usuarios.get_by_correo(data)
    if not user_in_db:
        flash("Correo/Contraseña erroneos")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.contrasena, request.form['contrasena']):
        flash("Correo/Contraseña erroneos")
        return redirect('/')
    session['usuario_id'] = user_in_db.id
    return redirect("/programa")

@app.route('/programa')
def programa():
    if "usuario_id" not in session:
        return redirect("/")
    id=session['usuario_id']
    data={
        "id":id
    }
    un_usuario=Usuarios.get_un_usuario(data)
    todos_programas=Programas.get_usuario_un_programa(data)
    return render_template("programa.html",todos_programas=todos_programas,un_usuario=un_usuario)



@app.route('/salir')
def sal():
    session.clear()
    return redirect('/')


@app.route('/crearprograma')
def nuevopro():
    if "usuario_id" not in session:
        return redirect("/")
    id=session['usuario_id']
    data={
        "id":id
    }
    un_usuario=Usuarios.get_un_usuario(data)
    now=datetime.now().strftime('%Y-%m-%d')
    return render_template("/crearprograma.html",un_usuario=un_usuario,now=now)


@app.route('/ver')
def mostrar():
    return render_template('/ver.html')
