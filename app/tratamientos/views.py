from django.shortcuts import render
from .models import Tratamiento

def lista_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, 'tratamientos/lista_tratamientos.html', {'tratamientos': tratamientos})

# Define otras funciones de vistas según sea necesario para el CRUD de tratamientos
