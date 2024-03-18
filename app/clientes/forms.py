from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre_apellido', 'edad', 'antecedentes_personales',
                  'antecedentes_hereditarios', 'alergia', 'medicacion']
