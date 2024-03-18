from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo de una ruta para mostrar la lista de clientes
    path('', views.lista_turnos, name='turnos'),
    # Aquí puedes agregar más rutas según sea necesario
]