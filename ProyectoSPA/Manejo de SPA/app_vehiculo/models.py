from django.db import models

# Create your models here.

from django.db import models

class Vehiculo(models.Model):
    
     ##Modelo que representa los vehículos del sistema

    modelo = models.IntegerField()
    marca = models.CharField(max_length=30)
    referencia = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    valor_comercial = models.BigIntegerField()

    def __str__(self):
        return self.referencia
    
        

class Event(models.Model):
    
    ##Modelo que representa eventos en el calendario

    title = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

