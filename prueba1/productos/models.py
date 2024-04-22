from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255,)
    descripcion = models.CharField(max_length=255,)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=255,)
    en_promocion = models.BooleanField()
    destacado = models.BooleanField()
