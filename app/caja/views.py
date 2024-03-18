from django.shortcuts import render
from .models import Caja

def lista_caja(request):
    movimientos_caja = Caja.objects.all()
    return render(request, 'caja/lista_caja.html', {'movimientos_caja': movimientos_caja})

# Define otras funciones de vistas según sea necesario para el CRUD de caja
