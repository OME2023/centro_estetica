from flask import request
from . import app, db
from .models import Cliente

@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    if request.method == 'POST':
        nuevo_cliente = Cliente(
            dni=request.form['dni'],
            nombre_apellido=request.form['nombre_apellido'],
            edad=request.form['edad'],
            antecedentes_personales=request.form['antecedentes_personales'],
            antecedentes_hereditarios=request.form['antecedentes_hereditarios'],
            alergia=request.form['alergia'],
            medicacion=request.form['medicacion'],
            # fecha_ingreso se asignará automáticamente al valor predeterminado
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return 'Cliente agregado exitosamente'
