from primer_app import app
from flask import render_template

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente 
def hola_mundo():                   # y a menos que no indiquemos otro metodo de consulta, es por default GET
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta


@app.route('/play')
def index():
    return render_template("index.html") #3 bloques azul


@app.route('/play/<int:numero>') #numero color azul 
def repetir_num(numero):
    return render_template('solonumero.html', numero=numero)



@app.route('/play/<int:numero>/<color>')
def repetir_prisma(numero, color):
    return render_template('jugar.html', numero=numero, color=color)



@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404