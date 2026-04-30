from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL

# Inicialización de Flask
app = Flask(__name__)

# CONFIGURACIÓN NECESARIA PARA FLASH (Añade esta línea)
app.secret_key = 'mi_llave_secreta_provisional'

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'contactanos_db'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':            
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Conexión y ejecución del CRUD
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        mysql.connection.commit()
        cur.close()
        
        flash('¡Contacto guardado exitosamente!')
        return render_template('contact.html') 
        
    return render_template('contact.html')

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)