from django.urls import path
from .views import cliente, producto, orden, inicio

urlpatterns = [
    path('inicio/', inicio),
    path('cliente/', cliente),
    path('producto/', producto),
    path('orden/', orden),
]
