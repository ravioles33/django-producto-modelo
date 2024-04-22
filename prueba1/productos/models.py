from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255,)
    descripcion = models.CharField(max_length=255,)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=255,)
    en_promocion = models.BooleanField()
    destacado = models.BooleanField()

class RandomLetter(models.Model):
    letter = models.CharField(max_length=1)  # Solo un carácter para la letra
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return self.letter