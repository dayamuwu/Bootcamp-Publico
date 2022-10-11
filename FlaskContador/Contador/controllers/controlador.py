from Contador import app
from flask import render_template, request, redirect, session
app.secret_key = 'ABC1234'


@app.route('/')
def contar():
    if 'contar' in session:
        session['contar']+=1
    else:
        session['contar']=1    
    return render_template("index.html")


@app.route("/destruir")
def dstr():
    session.clear()
    return redirect('/')


@app.route("/mas")
def mas():
    session['contar']+=1
    return redirect('/')


@app.route('/reinicio')
def reinicio():
    session.pop('contar')
    return redirect('/')


