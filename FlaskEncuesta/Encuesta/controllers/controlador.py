from Encuesta import app
from flask import render_template, request, redirect, session
app.secret_key = 'DFG5841'


@app.route('/')
def blabla():
    return render_template("index.html")