from . import db
from datetime import datetime, timezone

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    nombre_apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    antecedentes_personales = db.Column(db.Text, nullable=True)
    antecedentes_hereditarios = db.Column(db.Text, nullable=True)
    alergia = db.Column(db.Text, nullable=True)
    medicacion = db.Column(db.Text, nullable=True)
    fecha_ingreso = db.Column(db.DateTime, default=datetime.now(timezone.utc))

# En el archivo models.py

from . import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    nombre_apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    antecedentes_personales = db.Column(db.Text, nullable=True)
    antecedentes_hereditarios = db.Column(db.Text, nullable=True)
    alergia = db.Column(db.Text, nullable=True)
    medicacion = db.Column(db.Text, nullable=True)
    fecha_ingreso = db.Column(db.DateTime, default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'dni': self.dni,
            'nombre_apellido': self.nombre_apellido,
            'edad': self.edad,
            'antecedentes_personales': self.antecedentes_personales,
            'antecedentes_hereditarios': self.antecedentes_hereditarios,
            'alergia': self.alergia,
            'medicacion': self.medicacion,
            'fecha_ingreso': self.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S')  # Formatea la fecha como string
        }


# No olvides importar datetime si vas a usarlo para la fecha_ingreso
