from django import forms

from .models import Usuario

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Usuario
        fields = ["username", "first_name", "dni"]