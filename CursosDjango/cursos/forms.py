from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion','profesor','imagen','disponibilidad','precio','duracion']
        widgets = {
            'precio': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'step': '0.01',
                'placeholder': 'Ej. 499.99'
            })
        }
