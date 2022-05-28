"""
ENGLISH:
* Checky source code
    * The following source code was designed and coded by:
        * Feliciano Salazar Andrés Alberto
        * Martínez Godinez Ian Axel
        * Ramírez Pantoja Diego Alexey
        * Zamudio López Leonardo

        * Being students of the sixth semester of the technical career in 
        * Programming of the Center for Scientific and Technological Studies 9 
        * "Juan de Dios Bátiz" of the National Polytechnic Institute of Mexico.

        ! This code is licensed under the MIT license which can be read at 
        ! the file "LICENSE.md" of this repository


ESPAÑOL:
* Código fuente de Checky
    * El siguiente código fuente fue diseñado y codificado por:
        * Feliciano Salazar Andrés Alberto
        * Martínez Godinez Ian Axel
        * Ramírez Pantoja Diego Alexey
        * Zamudio López Leonardo

        * Siendo alumnos del sexto semestre de la carrera técnica en 
        * Programación del Centro de Estudios Científicos y Tecnológicos 9 
        * "Juan de Dios Bátiz" del Instituto Politécnico Nacional de México.

        ! Este código esta licenciado bajo la licencia MIT la cual puede ser leida en 
        ! el archivo "LICENSE.md" de este repositorio
"""

# ! Importacion de librerías (no borrar)
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)