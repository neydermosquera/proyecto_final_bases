from flask import Flask
from flask import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'proveedores'
mysql = MySQL(app)

@app.route('/')
def Index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)