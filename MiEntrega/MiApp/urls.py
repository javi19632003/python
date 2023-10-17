from django.urls import path
#from .views import cliente, producto, orden, inicio
from MiApp import views


urlpatterns = [
    #path('', views.inicio, name='Inicio'),
    path('', views.CursoListView.as_view(), name="List"),
    path('inicio/', views.CursoListView.as_view(), name='Inicio'),
    path('cliente/', views.cliente, name='Clientes'),
    path('producto/', views.producto, name='Productos'),
    path('buscar/', views.buscoproducto, name='BuscarProducto'),
    path('mostrar/', views.mostrarproducto, name='MostrarProducto'),
    path('registro/', views.register, name="Registro"),
    path('login/', views.login_request, name="Login"),
     path('orden/', views.orden),
]

# URL's basadas en clases
urlpatterns += [
    
    path('class-detalle-producto/<pk>/', views.CursoDetailView.as_view(), name="Pro_det"),
  #  path('class-crear-producto/', views.CursoCreateView.as_view(), name="Pro_Cre"),
  #  path('class-up-producto/<pk>/', views.CursoUpdateView.as_view(), name="Pro_Up"),
  #  path('class-del-producto/<pk>/', views.CursoDeleteView.as_view(), name="Pro_Del"),
]