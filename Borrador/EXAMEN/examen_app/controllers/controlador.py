from examen_app import app
from flask import render_template, request, redirect, session, flash
from examen_app.models.usuarios import Usuarios
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
app.secret_key = 'ch3st34r@'

@app.route('/')
def inicio():
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
#        if not Programas.validar_receta(request.form):
 #           return redirect("/recipes")
  #      Recipe.save_recipe(data)
   #     flash("Receta creada correctamente")
    #    return redirect('/recipes')