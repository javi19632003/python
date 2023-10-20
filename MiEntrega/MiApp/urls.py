from django.urls import path
#from .views import cliente, producto, orden, inicio
from MiApp import views
#from django.contrib.auth.views import LogoutView
#from django.conf import settings

urlpatterns = [
    #path('', views.inicio, name='Inicio'),
    path('', views.ProductoListView.as_view(), name="List"),
    path('inicio/', views.ProductoListView.as_view(), name='Inicio'),
    path('cliente/', views.cliente, name='Clientes'),
    path('producto/', views.producto, name='Productos'),
    path('buscar/', views.buscoproducto, name='BuscarProducto'),
    path('mostrar/', views.mostrarproducto, name='MostrarProducto'),
    path('registro/', views.register, name="Registro"),
    path('login/', views.login_request, name="Login"),
    path('logout/', views.logout_view, name="Logout"),
    path('orden/', views.orden),
]

# URL's basadas en clases
urlpatterns += [
    
    path('class-detalle-producto/<pk>/', views.ProductoDetailView.as_view(), name="Pro_Det"),
    path('class-crear-producto/', views.ProductoCreateView.as_view(), name="Pro_Cre"),
    path('class-up-producto/<pk>/', views.ProductoUpdateView.as_view(), name="Pro_Up"),
    path('class-del-producto/<pk>/', views.ProductoDeleteView.as_view(), name="Pro_Del"),
]