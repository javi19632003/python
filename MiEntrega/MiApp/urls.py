from django.urls import path
from MiApp import views

urlpatterns = [
    path('', views.ProductoListView.as_view(), name="List"),
    path('inicio/', views.ProductoListView.as_view(), name='List'),
    path('about/', views.about, name='About'),
    path('producto/',  views.ProductoCreateView.as_view(), name="Pro_Cre"),
    path('buscar/', views.buscoproducto, name='BuscarProducto'),
    path('registro/', views.register, name="Registro"),
    path('edit/', views.edit, name="Edit"),
    path('login/', views.login_request, name="Login"),
    path('logout/', views.logout_view, name="Logout"),
    path('agregar_carrito/<int:producto_id>/', views.agregar_carrito, name="add_carrito"),
    path('eliminar_carrito/<int:producto_id>/', views.eliminar_carrito, name="del_carrito"),
    path('restar_carrito/<int:producto_id>/', views.restar_carrito, name="sub_carrito"),
    path('limpiar_carrito/', views.limpiar_carrito, name="cls_carrito"),
    path('mirar_carrito/', views.mirar_carrito, name="read_carrito"),
]

# URL's basadas en clases
urlpatterns += [
    
    path('class-detalle-producto/<pk>/', views.ProductoDetailView.as_view(), name="Pro_Det"),
    path('class-up-producto/<pk>/', views.ProductoUpdateView.as_view(), name="Pro_Up"),
    path('class-del-producto/<pk>/', views.ProductoDeleteView.as_view(), name="Pro_Del"),
]