from django.urls import path
from MiApp import views

urlpatterns = [
    #path('', views.inicio, name='Inicio'),
    path('', views.ProductoListView.as_view(), name="List"),
    path('inicio/', views.ProductoListView.as_view(), name='List'),
    path('about/', views.about, name='About'),
    path('producto/',  views.ProductoCreateView.as_view(), name="Pro_Cre"),
    path('buscar/', views.buscoproducto, name='BuscarProducto'),
    path('mostrar/', views.mostrarproducto, name='MostrarProducto'),
    path('registro/', views.register, name="Registro"),
    path('login/', views.login_request, name="Login"),
    path('logout/', views.logout_view, name="Logout"),
   
]

# URL's basadas en clases
urlpatterns += [
    
    path('class-detalle-producto/<pk>/', views.ProductoDetailView.as_view(), name="Pro_Det"),
   # path('class-crear-producto/', views.ProductoCreateView.as_view(), name="Pro_Cre"),
    path('class-up-producto/<pk>/', views.ProductoUpdateView.as_view(), name="Pro_Up"),
    path('class-del-producto/<pk>/', views.ProductoDeleteView.as_view(), name="Pro_Del"),
]