from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


def conectar_bd():
    return mysql.connector.connect(
        host="mysql",
        user="usuario",
        password="password",
        database="zoologico"
    )


@app.route('/')
def index():

    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM animales")
    animales = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template('index.html', animales=animales)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)