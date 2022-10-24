'''
Flask [Python]
Ejercicios de profundizacion
Autor: Damian Safdie
Version: 1.0
 
'''

import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect
from flask_sqlalchemy import SQLAlchemy

import utils
import usuario


# Crear el server Flask
app = Flask(__name__)
# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///usuarios.db"
# Asociamos nuestro controlador de la base de datos con la aplicación
usuario.db.init_app(app)


@app.route("/user/{id}/titles__")
def titles__():
    try:
        pass
        return
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/user/titles__")
def titles__():
    try:
        #x, y = persona.dashboard()
        #image_html = utils.graficar(x, y)
        return Response(image_html.getvalue(), mimetype='image/png')
        
    except:
        return jsonify({'trace': traceback.format_exc()})




@app.before_first_request
def before_first_request_func():
    # Borrar y crear la base de datos
    usuario.db.create_all()
    usuario.db.drop_all()
    # Completar la base de datos
    usuario.fill()
    print("Base de datos generada")


if __name__ == '__main__':

    app.run(host="127.0.0.1", port=5000)



