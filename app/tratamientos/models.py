from django.db import models
from clientes.models import Cliente

class Tratamiento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad_sesiones = models.IntegerField(null=True)
    detalle = models.TextField()
    precio_unitario = models.FloatField()
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')],
        default='pendiente'
    )
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nombre_apellido} - {self.detalle}"

    class Meta:
        db_table = 'tratamientos'
