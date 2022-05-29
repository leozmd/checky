# Importación de librerías
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required

# Importación de archivo de configuración
from config import config

#Inicialización de la app
app = Flask(__name__)

# Inicialización de módulo de MySQL
db = MySQL(app)

# Inicialización de módulo de inicio de sesión
login_manager_app = LoginManager(app)

@app.route('/')
def index():
    res = redirect(url_for(login))
    return res

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('auth/login.html')