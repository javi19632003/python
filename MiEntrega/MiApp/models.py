from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre    = models.CharField(max_length=80)
    categoria = models.CharField(max_length=20)
    precio    = models.DecimalField(max_digits=19, decimal_places=2)

class Clientes(models.Model):
    nombre    = models.CharField(max_length=60)
    email     = models.EmailField(max_length=50)
    
class Ordenes(models.Model):
    nroord    = models.IntegerField()
    fecha     = models.DateTimeField()
    idprod    = models.IntegerField()
    idcliente = models.IntegerField()
    precio    = models.DecimalField(max_digits=19, decimal_places=2)
    
    