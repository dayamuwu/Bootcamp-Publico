from app_flask import app
from app_flask.models.usuarios import Usuarios
from app_flask.models.citas import Citas
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
app.secret_key = 'ch3st34r@'


@app.route('/')
def inicio():
    if 'id_usuario' not in session:
        return render_template("index.html")


@app.route('/salir')
def logout():
    if "usuario_id" not in session:
        return redirect("/")
    session.clear()
    return redirect('/')



@app.route('/crear', methods=['POST'])
def crear():
    valor=request.form['formu']
    if valor == "usuarios":
        pw_hash = bcrypt.generate_password_hash(request.form['contrasena'])
        data = {
            "nombre": request.form['nombre'],
            "correo": request.form['correo'],
            "contrasena" : pw_hash
        }
        if not Usuarios.validar_usuario(request.form):
            return redirect("/")
        usuario_id = Usuarios.guardar_usuario(data)
        session['usuario_id'] = usuario_id
        flash("Usuario creado correctamente, ahora puedes logearte")
        return redirect('/')
    elif valor == "citas":
        data = {
            "tareas":request.form["tareas"],
            "fecha":request.form["fecha"],
            "estado":request.form["estado"],
            "usuario_id":session['usuario_id'],
            }
        if not Citas.validar_cita(request.form):
            return redirect("/")
        Citas.guardar_cita(data)
        flash("Cita creada correctamente")
        return redirect('/citas') 



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
    return redirect("/bienvenida")

@app.route('/bienvenida')
def welcome():
    if "usuario_id" not in session:
        return redirect("/")
    id=session['usuario_id']
    data={
        "id":id
    }
    un_usuario = Usuarios.get_un_usuario(data)
    return render_template('bienvenida.html', un_usuario=un_usuario)


@app.route('/crear_cita')
def crear_cita():
    return render_template('crear_cita.html')


@app.route('/citas')
def cita():
    if "usuario_id" not in session:
        return redirect("/")
    id=session['usuario_id']
    data={
        "id":id
    }
    todas_citas=Citas.get_all_citas()
    un_usuario = Usuarios.get_un_usuario(data)
    return render_template('citas.html', un_usuario=un_usuario, todas_citas=todas_citas)


@app.route('/borrar/<int:id>')
def borrar(id):
    if "usuario_id" not in session:
        return redirect("/")
    data = {
        'id': id,
    }
    Citas.borrar_cita(data)
    flash("Cita borrada correctamente")
    return redirect('/citas')





@app.route('/editar/<int:id>')
def editar(id):
    if "usuario_id" not in session:
        return redirect("/")
    iduser=session['usuario_id']
    newdata={"id":iduser}
    data = {
        'id' : id
    }
    una_cita=Citas.get_una_cita(data)
    return render_template("/editar.html", una_cita=una_cita)


@app.route('/editar/<int:id>', methods=['POST'])
def edit(id):
    if "usuario_id" not in session:
        return redirect("/")
    data = {
        'id' : id,
        "tareas": request.form["tareas"],
        "fecha" : request.form["fecha"],
        "estado" : request.form["estado"],
    }
    if not Citas.validar_cita(request.form):
        return redirect("/")
    Citas.update(data)
    return redirect("/citas")





