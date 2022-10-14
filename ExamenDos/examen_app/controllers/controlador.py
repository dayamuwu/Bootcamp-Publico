from calendar import day_abbr
from datetime import date,datetime
from examen_app.models.viajes import Viajes
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
    elif valor == "Viajes":
        data = {
            "plan":request.form["plan"],
            "inicio_viaje":request.form["inicio_viaje"],
            "fin_viaje":request.form["fin_viaje"],
            "descripcion":request.form["descripcion"],
            "usuario_id":session['usuario_id'],
            }
        if not Viajes.validar_viaje(request.form):
            return redirect("/ver")
        Viajes.guardar_viaje(data)
        flash("Viaje creado correctamente")
        return redirect('/ver') 


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
    return redirect("/ver")

@app.route('/ver')
def ver():
    if "usuario_id" not in session:
        return redirect("/")
    id=session['usuario_id']
    data={
        "id":id
    }
    un_usuario=Usuarios.get_un_usuario(data)
    todos_viajes=Viajes.get_usuario_viaje()
    return render_template("ver.html",todos_viajes=todos_viajes,un_usuario=un_usuario)


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


@app.route('/ver/<int:id>')
def mostrar(id):
    if "usuario_id" not in session:
        return redirect("/")
    iduser=session['usuario_id']
    newdata={"id":iduser}
    data={
        "id":id
    }
    un_usuario=Usuarios.get_un_usuario(newdata)
    todos_viajes=Viajes.get_usuario_un_viajes(data)
    return render_template("ver.html",todos_viajes=todos_viajes,un_usuario=un_usuario)


#@app.route('/ver/editar/<int:id>')
#def editar(id):
#    if "usuario_id" not in session:
#        return redirect("/")
#    iduser=session['usuario_id']
#    newdata={"id":iduser}
#    data = {
#        'id' : id
#        }
#    un_usuario=Usuarios.get_un_usuario(newdata)
#    un_viaje=Viajes.get_un_viaje(data)
#    fecha=str(un_viaje.created_at)
#    now=datetime.now().strftime('%Y-%m-%d')
#    checkedsi=""
#    checkedno=""
#    if un_viaje.created_at==1:
#        checkedsi="checked"
#    if un_viaje.created_at==2:
#        checkedno="checked"
#    return render_template("editar.html",programa=Viajes.get_un_viaje(data),un_usuario=un_usuario,fecha=fecha,checkedsi=checkedsi,checkedno=checkedno,now=now)


#@app.route('/editar/<int:id>', methods=['POST'])
#def editars(id):
#    if "usuario_id" not in session:
#        return redirect("/")
#    data = {
#        'id' : id,
#        "titulo": request.form["titulo"],
#        "canal" : request.form["canal"],
#        "lanzamiento" : request.form["lanzamiento"],
#        "descripcion":request.form["descripcion"],
#    }
#    Viajes.update(data)
#    return redirect("/programa")


@app.route('/borrar/<int:id>')
def borrar(id):
    if "usuario_id" not in session:
        return redirect("/")
    data = {
        'id': id,
    }
    Viajes.destruir_viaje(data)
    flash("Viaje borrado correctamente")
    return redirect('/programa')


@app.route('/salir')
def sal():
    if "usuario_id" not in session:
        return redirect('/')
    session.clear()
    return redirect('/')
