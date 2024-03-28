from . import db
import datetime

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
    fecha_ingreso = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# No olvides importar datetime si vas a usarlo para la fecha_ingreso
