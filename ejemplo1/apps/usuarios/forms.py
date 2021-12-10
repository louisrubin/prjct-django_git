from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from .models import Usuario

class ProductoForm(forms.ModelForm):
    #nombre = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "dni"]
        labels = {"username": "Nombre de Usuario", "first_name": "Apellido", "dni": "DNI",}


class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'dni'
            ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'dni': 'DNI',
            }