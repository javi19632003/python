from typing import Any
from django.shortcuts            import render
from django.http                 import HttpResponse
from MiApp.forms                 import ClienteForm, ProductoForm, BuscaProductoForm, UserRegisterForm
from .models                     import Clientes, Productos, User1
from django.views.generic        import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit   import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms   import AuthenticationForm
from django.contrib.auth         import login, authenticate
from django.contrib.auth.views   import LogoutView
from django.contrib.auth         import logout
from .context_processors         import custom_avatar

def inicio(request):
    mis_productos = Productos.objects.all()
    data = {
            "productos":mis_productos,
           }
    return render(request, "MiApp/resultados_class.html", data)

def orden(request):
    return HttpResponse("alta orden!")

# Vista basada en funciones
def cliente (request) :
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
    
        if miForm.is_valid():
            datos = miForm.cleaned_data
            cliente = Clientes(nombre=datos["nombre"], email=datos["email"])
            cliente.save()
            mis_productos = Productos.objects.all()
            return render(request, "MiApp/resultados_class.html", {"productos":mis_productos})
    else:
        miForm = ClienteForm()

    return render(request, "MiApp/form_api.html", {"miForm": miForm}) 

# Vista basada en funciones
def producto (request) :
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
    
        if miForm.is_valid():
            datos = miForm.cleaned_data
            producto = Productos(nombre=datos["nombre"], categoria=datos["categoria"], precio=datos["precio"])
            producto.save()
            mis_productos = Productos.objects.all()
            return render(request, "MiApp/resultados_class.html", {"productos":mis_productos})
    else:
        miForm = ProductoForm()

    return render(request, "MiApp/form_api.html", {"miForm": miForm}) 

# Vista basada en funciones
def buscoproducto(request):
    if request.method == "POST":
        miForm = BuscaProductoForm(request.POST) 
        
        if miForm.is_valid():
            dato = miForm.cleaned_data
            
            mis_productos = Productos.objects.filter(nombre__icontains=dato["nombre"])
            
            data = {
                   "productos":mis_productos,
                }

            return render(request, "MiApp/resultados.html", data)
    else:
        miForm = BuscaProductoForm()

    return render(request, "MiApp/form_api.html", {"miForm": miForm})


def mostrarproducto(request):
    return HttpResponse("mostrando!")

# Vistas con clases

class ProductoListView(ListView):
    model = Productos
    template_name = "MiApp/resultados_class.html"
    
class ProductoDetailView(DetailView):
    model = Productos
    template_name = "MiApp/detalle_class.html"    

   
def logout_view(request):
    logout(request)
    mis_productos = Productos.objects.all()
    return render(request, "MiApp/resultados.html", {"productos":mis_productos})
        
def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            mis_productos = Productos.objects.all()
   
            return render(request, "MiApp/resultados_class.html", {"productos":mis_productos})
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"Miapp/registro.html" ,  {"form":form, "msg_register": msg_register})
    
def login_request(request):
    msg_login = ""

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            print("entre en login")    
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                mis_productos = Productos.objects.all()
                data = {
                    "productos":mis_productos,
                }
                
                return render(request, "MiApp/resultados.html", data)

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    
    data = { "form": form, 
             "msg_login": msg_login
           }
    
    return render(request, "Miapp/login.html", data)    

    