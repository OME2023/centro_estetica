from django.db import models

class Cliente(models.Model):
    dni = models.CharField(max_length=20)
    nombre_apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True)
    antecedentes_personales = models.TextField(null=True)
    antecedentes_hereditarios = models.TextField(null=True)
    alergia = models.TextField(null=True)
    medicacion = models.TextField(null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_apellido
    
    class Meta:
        db_table = 'clientes'