from django import forms

from .models import Usuario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "dni"]