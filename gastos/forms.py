from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'fecha', 'categoria', 'nota']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'nota': forms.Textarea(attrs={'rows':3}),
        }
