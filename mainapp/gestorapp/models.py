from django.db import models
import bcrypt
import datetime
from django import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    registered_on = models.DateTimeField()
    admin = models.BooleanField()
    
    # def __init__(self, *args, **kwargs):
    #     self.fields['password'].disabled = True
    #     self.fields['additional_field'].initial = 'SOME INITIAL VALUE'
    
    def __str__(self) -> str:
        return f"Usuario {self.id} {self.email} {self.password} {self.registered_on} {self.admin}"
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    duracion = models.CharField(max_length=10)
    portada = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"Pelicula {self.id} {self.titulo} {self.duracion} {self.portada} {self.director}"