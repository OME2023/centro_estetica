from django.db import models

class Caja(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"${self.monto} - {self.fecha}"
    
    class Meta:
        db_table = 'caja'