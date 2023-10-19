from django.db                  import models
from django.contrib.auth.models import User
from django.conf                import settings
# Create your models here.
class Productos(models.Model):
    nombre     = models.CharField(max_length=80)
    categoria  = models.CharField(max_length=20)
    precio     = models.DecimalField(max_digits=19, decimal_places=2)
    descrip    = models.TextField(blank=True)
    imagen     = models.ImageField(upload_to='productos', null=True, blank = True)
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"

class Clientes(models.Model):
    nombre    = models.CharField(max_length=60)
    email     = models.EmailField(max_length=50 , unique=True)
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"

class User1(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
    def dame_ruta(self):
        return f"{settings.MEDIA_URL}{self.imagen}"
    
class Ordenes(models.Model):
    nroord    = models.IntegerField()
    fecha     = models.DateTimeField()
    idprod    = models.IntegerField()
    idcliente = models.IntegerField()
    precio    = models.DecimalField(max_digits=19, decimal_places=2)
    
    