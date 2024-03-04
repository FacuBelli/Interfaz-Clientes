import pyodbc
from flask import Flask, render_template, request

# Conexión a la base de datos
server = 'tu_servidor'
database = 'tu_base_de_datos'
username = 'tu_usuario'
password = 'tu_contraseña'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        # Aquí puedes ejecutar tu consulta SQL para agregar un cliente
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nombre) VALUES (?)", (nombre,))
        conn.commit()
        cursor.close()
        return 'Cliente agregado correctamente'

if __name__ == '__main__':
    app.run(debug=True)
