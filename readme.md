# Sistema de Ventas y Cálculo de Sueldo

Proyecto desarrollado en **Python (Flask)** con **MySQL** como base de datos.  
El sistema permite:
- Calcular sueldos con comisiones y extras.
- Registrar nuevas ventas en una base de datos.
- Buscar y filtrar ventas con distintos criterios.
- Navegar entre secciones desde un menú principal.

---

## 🚀 Tecnologías utilizadas
- Python 3
- Flask
- MySQL
- HTML / CSS (Jinja2 templates)

---

## 📂 Estructura del proyecto
mi-sistema-ventas/
│
├── app.py                 # servidor Flask con todas las rutas
├── logica.py              # funciones de cálculo de sueldo
├── templates/             # páginas HTML
│   ├── base.html
│   ├── menu.html
│   ├── index.html
│   ├── resultado.html
│   ├── nueva_venta.html
│   ├── buscar_ventas.html
│   └── resultado_busqueda.html
├── static/                # archivos estáticos
│   └── style.css
└── schema.sql             # estructura de la base de datos


---

## 🛠️ Instalación y configuración

**Clonar el repositorio**

git clone https://github.com/tuusuario/mi-sistema-ventas.git
cd mi-sistema-ventas

Instalar dependencias

pip install flask mysql-connector-python

Configurar la base de datos
Crear una base de datos en MySQL:

CREATE DATABASE mi_base;
USE mi_base;
Importar la estructura desde schema.sql:

schema.sql
Configurar conexión en app.py

python
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TU_PASSWORD",
    database="mi_base"
)
▶️ Ejecución
Iniciar el servidor Flask:
python app.py

Abrir en el navegador:

http://127.0.0.1:5000/