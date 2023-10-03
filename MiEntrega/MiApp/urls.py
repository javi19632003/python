from django.urls import path
#from .views import cliente, producto, orden, inicio
from MiApp import views
urlpatterns = [
    path('inicio/', views.inicio, name='Inicio'),
    path('cliente/', views.cliente, name='Clientes'),
    path('producto/', views.producto, name='Productos'),
    path('buscar/', views.buscoproducto, name='BuscarProducto'),
    path('mostrar/', views.mostrarproducto, name='MostrarProducto'),
     path('orden/', views.orden),
]
