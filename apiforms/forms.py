from django import forms
from .models import Busqueda, Resultado


class BusquedaForm(forms.ModelForm):
    class Meta:
        model = Busqueda
        fields = ['busqueda', 'precio_min', 'precio_max']