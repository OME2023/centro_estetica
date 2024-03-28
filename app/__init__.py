from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Asegúrate de usar el path correcto para tu archivo de base de datos, dependiendo de tu sistema operativo y estructura de proyecto
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes  # Importa las rutas
        db.create_all()  # Crea las tablas basadas en los modelos si no existen

    return app
