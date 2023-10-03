from django.contrib import admin
from .models import Productos, Clientes, Ordenes
# Register your models here.
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Ordenes)