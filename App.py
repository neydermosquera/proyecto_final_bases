from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_mysqldb import MySQL


app = Flask(__name__)


#MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'usuarioprueba'
app.config['MYSQL_PASSWORD'] = 'bases2020'
app.config['MYSQL_DB'] = 'aerolinea'
mysql = MySQL(app)

#Sesion 
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout.html')
def layout():
    return render_template('layout.html')

@app.route('/consultas.html')
def consultas():
    return render_template('consultas.html')

@app.route('/rutas.html')
def rutas():
    return render_template('rutas.html')

@app.route('/registro.html')
def registro():
    return render_template('registro.html')

@app.route('/formpasajero.html')
def formpasajero():
    return render_template('formpasajero.html')


@app.route('/registro.html/agregar_pasajero', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        print(nombre)
        print(apellido)
        print(telefono)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (nombre, apellido, telefono) VALUES (%s, %s, %s)', (nombre, apellido, telefono))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('formularios'))


@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete/<string:id>')
def delete_contact(id):
    return id


if __name__ == '__main__':
    app.run(port = 3000, debug = True) 