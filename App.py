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

@app.route('/formempleado.html')
def formempleado():
    return render_template('formempleado.html')

@app.route('/formruta.html')
def formruta():
    return render_template('formruta.html')

@app.route('/formpasajeVuelo.html')
def formpasajeVuelo():
    return render_template('formpasajeVuelo.html')

@app.route('/formmarca.html')
def formmarca():
    return render_template('formmarca.html')

@app.route('/formestadovuelo.html')
def formestadoVuelo():
    return render_template('formestadovuelo.html')

@app.route('/formcargo.html')
def formcargo():
    return render_template('formcargo.html')

@app.route('/formavion.html')
def formavion():
    return render_template('formavion.html')

@app.route('/consultapasajero.html')
def consultapasajero():
    return render_template('consultapasajero.html')


@app.route('/registro.html/agregar_marca', methods=['POST'])
def add_marca():
    if (request.method) == 'POST':
        descripcion = request.form['descripcion']
        print(descripcion)
        cur = mysql.connection.cursor()
        cur.callproc('agregarMarca', [descripcion])
        mysql.connection.commit()
        flash('Nueva MARCA agregada satisfactoriamente')
        return redirect(url_for('formmarca'))

@app.route('/registro.html/agregar_cargo', methods=['POST'])
def add_cargo():
    if (request.method) == 'POST':
        descripcion = request.form['descripcion']
        print(descripcion)
        cur = mysql.connection.cursor()
        cur.callproc('agregarCargo', [descripcion])
        mysql.connection.commit()
        flash('Nueva CARGO agregado satisfactoriamente')
        return redirect(url_for('formcargo'))

@app.route('/resultadopasajero.html', methods=['POST'])
def resultadoPasajero():
    if request.method == 'POST':
        documento = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute("""SELECT per.* FROM persona per, pasajero pas 
                    WHERE per.numerodocumento = %s AND
                    per.idpersona = pas.idpasajero """, (documento))
        data = cur.fetchall()
    return render_template('resultadopasajero.html', persona = data)

@app.route('/consultamarca.html')
def consultaMarca():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM marca')
    data = cur.fetchall()
    return render_template('consultamarca.html', marca = data)

@app.route('/consultacargo.html')
def consultaCargo():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cargo')
    data = cur.fetchall()
    return render_template('consultaCargo.html', cargo = data)

@app.route('/deletecargo/<string:id>')
def deleteCargo(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cargo WHERE idcargo = {0}'.format(id))
    mysql.connection.commit()
    flash('CARGO eliminado con éxito')
    return redirect(url_for('consultaCargo'))

@app.route('/editcargo/<id>')
def getCargo(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cargo WHERE idcargo = %s', (id))
    data = cur.fetchall()
    return render_template('editcargo.html', carg = data[0])

@app.route('/updatecargo/<id>', methods=['POST'])
def updateCargo(id):
    if request.method == 'POST':
        nombre = request.form['descripcion']
    cur = mysql.connection.cursor()
    cur.execute(""" 
        UPDATE cargo
        SET nombre = %s 
        WHERE idcargo = %s
    """, (nombre, id))
    mysql.connection.commit()
    flash('CARGO actualizado con éxito')
    return redirect(url_for('consultaCargo'))
   

@app.route('/delete/<string:id>')
def delete_cargo(id):
    return id

def mostrarPaises():
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre FROM pais')
    paises = cur.fetchall()
    print(paises)


if __name__ == '__main__':
    app.run(port = 3000, debug = True) 