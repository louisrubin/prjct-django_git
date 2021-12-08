from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Usuario(models.Model):
    nombre = CharField(max_length=50)
    user_name = CharField(max_length=50)
    edad = IntegerField(max_length=10)
