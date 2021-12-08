from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(null=True, blank= True)
    # foto = models.ImageField()

    class Meta:
        db_table = 'usuarios'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
