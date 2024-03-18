from django.shortcuts import render
from .models import Turno

def lista_turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'turnos/lista_turnos.html', {'turnos': turnos})

# Define otras funciones de vistas según sea necesario para el CRUD de turnos
