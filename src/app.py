# Importación de librerías
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

# Importación de archivo de configuración
from config import config

# Modelos
from models.ModelUser import ModelUser

# Entidades
from models.entities.User import User

#Inicialización de la app
app = Flask(__name__, static_url_path="", static_folder="static")

# Inicialización de protección contra CSRF
csrf = CSRFProtect(app)

# Inicialización de módulo de MySQL
db = MySQL(app)

# Inicialización de módulo de inicio de sesión
login_manager_app = LoginManager(app)

# Función para obtener datos de usuario activo
@login_manager_app.user_loader
def load_user(idUsuario):
    return ModelUser.getById(db, idUsuario)

# Ruta raiz
@app.route('/')
def index():
    res = redirect(url_for('login'))
    return res

# Ruta login con métodos GET y POST
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User(0,"", "", "", "", "",request.form['usuUsuario'], request.form['passUsuario'],0,0)
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.passUsuario:
                login_user(logged_user)
                return redirect(url_for('adminInicio'))
            else:
                flash("Contraseña incorrecta")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# Ruta logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Ruta principal de administrador
@app.route('/admin')
@login_required
def adminInicio():
    return render_template('admin/admin_inicio.html')

@app.route('/admin/asignaturas')
@login_required
def adminAsignaturas():
    return render_template('admin/admin_ver_asignaturas.html')

@app.route('/admin/carreras')
@login_required
def adminCarreras():
    return render_template('admin/admin_ver_carreras.html')

@app.route('/admin/clases')
@login_required
def adminClases():
    return render_template('admin/admin_ver_clases.html')

@app.route('/admin/estados')
@login_required
def adminEstados():
    return render_template('admin/admin_ver_estados.html')

@app.route('/admin/grados')
@login_required
def adminGrados():
    return render_template('admin/admin_ver_grados.html')

@app.route('/admin/grupos')
@login_required
def adminGrupos():
    return render_template('admin/admin_ver_grupos.html')

@app.route('/admin/horarios')
@login_required
def adminHorarios():
    return render_template('admin/admin_ver_horarios.html')

@app.route('/admin/reportes')
@login_required
def adminReportes():
    return render_template('admin/admin_ver_reportes.html')

@app.route('/admin/turnos')
@login_required
def adminTurnos():
    return render_template('admin/admin_ver_turnos.html')

@app.route('/admin/usuarios')
@login_required
def adminUsuarios():
    return render_template('admin/admin_ver_usuarios.html')

@app.route('/admin/asignaturas/crear')
@login_required
def crearAsignatura():
    return render_template('admin/crear_asignatura.html')

@app.route('/admin/carreras/crear')
@login_required
def crearCarrera():
    return render_template('admin/crear_carrera.html')

@app.route('/admin/clases/crear')
@login_required
def crearClase():
    return render_template('admin/crear_clase.html')

@app.route('/admin/estados/crear')
@login_required
def crearEstado():
    return render_template('admin/crear_estado.html')

@app.route('/admin/grados/crear')
@login_required
def crearGrado():
    return render_template('admin/crear_grado.html')

@app.route('/admin/grupos/crear')
@login_required
def crearGrupo():
    return render_template('admin/crear_grupo.html')

@app.route('/admin/horarios/crear')
@login_required
def crearHorario():
    return render_template('admin/crear_horario.html')

@app.route('/admin/turnos/crear')
@login_required
def crearTurno():
    return render_template('admin/crear_turno.html')

@app.route('/admin/usuarios/crear')
@login_required
def crearUsuario():
    return render_template('admin/crear_usuario.html')

@app.route('admin/asignaturas/editar/<int:idAsignatura>')
@login_required
def editarAsignatura(idAsignatura):
    return render_template("admin/editar_asignatura.html")

@app.route('admin/carreras/editar/<int:idCarrera>')
@login_required
def editarCarrera(idCarrera):
    return render_template("admin/editar_carrera.html")

@app.route('admin/clases/editar/<int:idClase>')
@login_required
def editarClase(idClase):
    return render_template("admin/editar_clase.html")

@app.route('admin/estados/editar/<int:idEstado>')
@login_required
def editarEstado(idEstado):
    return render_template("admin/editar_estado.html")

@app.route('admin/grados/editar/<int:idGrado>')
@login_required
def editarGrado(idGrado):
    return render_template("admin/editar_grado.html")

@app.route('admin/grupos/editar/<int:idGrupo>')
@login_required
def editarGrupo(idGrupo):
    return render_template("admin/editar_grupo.html")

@app.route('admin/horarios/editar/<int:idHorario>')
@login_required
def editarHorario(idHorario):
    return render_template("admin/editar_horario.html")

@app.route('admin/turnos/editar/<int:idTurno>')
@login_required
def editarTurno(idTurno):
    return render_template("admin/editar_turno.html")

@app.route('admin/usuarios/editar/<int:idUsuario>')
@login_required
def editarUsuario(idUsuario):
    return render_template("admin/editar_usuario.html")

# Método para error 404 (Not Found)
def status_404(error):
    return render_template('404.html')

#Metodo para error 401 (Unauthorized)
def status_401(error):
    return redirect(url_for('index'))

# Parámetros de ejecución
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()