from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre     = models.CharField(max_length=80)
    categoria  = models.CharField(max_length=20)
    precio     = models.DecimalField(max_digits=19, decimal_places=2)
    descrip    = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"

class Clientes(models.Model):
    nombre    = models.CharField(max_length=60)
    email     = models.EmailField(max_length=50 , unique=True)
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"
    
class Ordenes(models.Model):
    nroord    = models.IntegerField()
    fecha     = models.DateTimeField()
    idprod    = models.IntegerField()
    idcliente = models.IntegerField()
    precio    = models.DecimalField(max_digits=19, decimal_places=2)
    
    