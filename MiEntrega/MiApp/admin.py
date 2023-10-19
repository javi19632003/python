from django.contrib import admin
from .models import Productos, Clientes, Ordenes, User1
# Register your models here.
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Ordenes)
admin.site.register(User1)