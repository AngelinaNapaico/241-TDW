# Proyecto: Formulario de Contacto con Flask y MySQL

Este proyecto es una aplicación web funcional que permite la gestión de mensajes de contacto. Ha sido desarrollado como parte de la evaluación de **Tecnologia Digital Web**, cumpliendo con los estándares de persistencia de datos y diseño responsivo.

## Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado:
* **Python 3.x**
* **MySQL Server**
* **Entorno virtual (venv)**

## Configuración y Ejecución

Sigue estos pasos para poner en marcha el proyecto en GitHub Codespaces:

### 1. Iniciar el servicio de Base de Datos
Es necesario arrancar el motor de MySQL antes de iniciar la aplicación Flask:
```bash
sudo service mysql start
```

### 2. Preparar la Base de Datos 
Importa el script proporcionado para crear la estructura necesaria:
```bash
sudo mysql -u root -p < database.sql
(La contraseña configurada es 123456)
```

### 3. Activar el Entorno Virtual e Instalar Dependencias
```bash
source venv/bin/activate
pip install flask flask-mysqldb
```

### 4. Generar Estilos (Tailwind CSS)
```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css
```

### 5. Iniciar la Aplicación
```bash
python app.py

## **Angelina Napaico Valencia**