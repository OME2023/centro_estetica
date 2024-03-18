from django.db import models
from clientes.models import Cliente

class Turno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.cliente.nombre_apellido} - {self.fecha}"

    class Meta:
        db_table = 'turno'