from flask import Flask
from flask_mysqldb import MySQL
import requests # type: ignore
# inicializacion de mi frameword flask
app = Flask(__name__)
# configuracion de mysql
mysql=MySQL(app)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']=3306
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='contactanos_db'
mysql.init_app(app)

@app.route('/' , methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':            
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

 # Aqui puedes agregar la logica para guardar los datos en la base de datos
    cur = mysql.connection.cursor()
    mysql.connection.commit()
    cur.close()
    flash('Contacto guardado exitosamente!')
    return render_template('contact.html')
# ejecutar mi servidor
if __name__ == '__main__':
    app.run(debug=True)
