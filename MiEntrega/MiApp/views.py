from typing import Any
from django.shortcuts            import render
from django.http                 import HttpResponse
from MiApp.forms                 import ProductoForm, BuscaProductoForm, UserRegisterForm
from .models                     import Productos, User1

from django.contrib.auth.forms   import AuthenticationForm
from django.contrib.auth         import login, authenticate
#from django.contrib.auth.views   import LogoutView
from django.contrib.auth         import logout
#from .context_processors         import custom_avatar
# Import de vistas basadas en clases 
from django.views.generic        import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit   import CreateView, UpdateView, DeleteView
from django.urls                 import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    mis_productos = Productos.objects.all()
    data = {
            "productos":mis_productos,
           }
    return render(request, "MiApp/resultados_class.html", data)

def about(request):
    return HttpResponse("acerca de !")



# Vista basada en funciones
@login_required
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
# Busca los productos que tengan concidencias en el nombre con el string buscado
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

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = "MiApp/producto_create.html"
    fields = ["nombre", "categoria", "precio", "descrip", "imagen" ]
    success_url = reverse_lazy("List")

def mostrarproducto(request):
    return HttpResponse("mostrando!")

# Vistas con clases

class ProductoListView(ListView):
    model = Productos
    template_name = "MiApp/resultados_class.html"
    
class ProductoDetailView(DetailView):
    model = Productos
    template_name = "MiApp/detalle_class.html" 
    

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = reverse_lazy("List")
    template_name = 'MiApp/producto_delete.html'

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Productos
    success_url = reverse_lazy("List")
    fields = ["nombre", "categoria", "precio", "descrip", "imagen" ]
    template_name = "MiApp/producto_update.html"   

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
            #User1.objects.create(imagen= " ", user=form.data["username"])
            mis_productos = Productos.objects.all()
            return render(request, "MiApp/resultados.html", {"productos":mis_productos})
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"Miapp/registro.html" ,  {"form":form, "msg_register": msg_register})
    
def login_request(request):
    msg_login = ""

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                mis_productos = Productos.objects.all()
                return render(request, "MiApp/resultados.html", {"productos":mis_productos})

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    
    data = { "form": form, 
             "msg_login": msg_login
           }
    
    return render(request, "Miapp/login.html", data)    

    