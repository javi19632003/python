from django.urls import path
#from .views import cliente, producto, orden, inicio
from MiApp import views


urlpatterns = [
    path('', views.inicio, name='Inicio'),
   #path('inicio/', views.inicio, name='Inicio'),
    path('cliente/', views.cliente, name='Clientes'),
    path('producto/', views.producto, name='Productos'),
    path('buscar/', views.buscoproducto, name='BuscarProducto'),
    path('mostrar/', views.mostrarproducto, name='MostrarProducto'),
     path('orden/', views.orden),
]

# URL's basadas en clases
urlpatterns += [
    path('class-inicio/', views.CursoListView.as_view(), name="List"),
    path('class-detalle-producto/<pk>/', views.CursoDetailView.as_view(), name="Pro_det"),
  #  path('class-crear-producto/', views.CursoCreateView.as_view(), name="Pro_Cre"),
  #  path('class-up-producto/<pk>/', views.CursoUpdateView.as_view(), name="Pro_Up"),
  #  path('class-del-producto/<pk>/', views.CursoDeleteView.as_view(), name="Pro_Del"),
]