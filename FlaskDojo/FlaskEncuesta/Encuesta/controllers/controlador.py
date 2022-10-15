from Encuesta import app
from flask import render_template, request, redirect, session
app.secret_key = 'DFG5841'


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/proceso', methods=['POST'])
def prcs():
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicacion']
    session['lenguaje'] = request.form['lenguaje']
    session['comentario'] = request.form['comentario']
    return redirect('/resultado')

@app.route('/resultado', methods=['GET'])
def rsd():
    nombre=session['nombre']
    ubicacion=session['ubicacion']
    lenguaje=session['lenguaje']
    comentario=session['comentario']
    return render_template('resultado.html', nombre=nombre, ubicacion=ubicacion, lenguaje=lenguaje, comentario=comentario)


@app.route('/back')
def bck():
    return redirect('/')

