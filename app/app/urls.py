"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),  # Rutas de la aplicación 'clientes'
    path('tratamientos/', include('tratamientos.urls')),  # Rutas de la aplicación 'tratamientos'
    path('turnos/', include('turnos.urls')),  # Rutas de la aplicación 'turnos'
    path('caja/', include('caja.urls')),  # Rutas de la aplicación 'caja'
]