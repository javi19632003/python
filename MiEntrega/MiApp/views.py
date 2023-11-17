from typing import Any
from django.shortcuts            import render
from django.http                 import HttpResponse
from MiApp.forms                 import ProductoForm, BuscaProductoForm, UserRegisterForm, UserEditForm
from .models                     import Productos, User1
from CarritoApp.carrito          import Carrito
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
from django.shortcuts import redirect

def inicio(request):
    mis_productos = Productos.objects.all()
    data = {
            "productos":mis_productos,
           }
    return render(request, "MiApp/resultados_class.html", data)

def about(request):
    return render(request, "MiApp/about.html")

# Vista basada en funciones
@login_required
def producto (request) :
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
    
        if miForm.is_valid():
            datos = miForm.cleaned_data
            producto = Productos(nombre=datos["nombre"], categoria=datos["categoria"], precio=datos["precio"])
            producto.save()
            return redirect('List')
            #mis_productos = Productos.objects.all()
            #return render(request, "MiApp/resultados_class.html", {"productos":mis_productos})
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
            return redirect('List')
           # mis_productos = Productos.objects.all()
           # return render(request, "MiApp/resultados.html", {"productos":mis_productos})
        
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
                return redirect('List')
                #mis_productos = Productos.objects.all()
                #return render(request, "MiApp/resultados.html", {"productos":mis_productos})

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    
    data = { "form": form, 
             "msg_login": msg_login
           }
    
    return render(request, "Miapp/login.html", data)    

    
# Vista de editar el perfil
@login_required
def edit(request):
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
 
            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'last_name': usuario.last_name,
                    'email': usuario.email
                    
                }
                miFormulario = UserEditForm(initial=datos)

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()

                # Creamos nueva imagen en la tabla
                try:
                    avatar = User1.objects.get(user=usuario)
                except User1.DoesNotExist:
                    avatar = User1(user=usuario, imagen=informacion["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = informacion["imagen"]
                    avatar.save()
                    return redirect('List')
                    #mis_productos = Productos.objects.all()
                    #return render(request, "MiApp/resultados.html", {"productos":mis_productos})
                
    else:
        datos = {
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "MiApp/editar_usuario.html", {"mi_formulario": miFormulario, "usuario": usuario})



@login_required
def agregar_carrito (request, producto_id) :
    carrito  = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('List')

@login_required
def eliminar_carrito (request, producto_id) :
    carrito  = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('List')

@login_required
def restar_carrito (request, producto_id) :
    carrito  = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('List')

@login_required
def limpiar_carrito (request) :
    carrito  = Carrito(request)
    carrito.limpar()
    return redirect('List')

@login_required
def mirar_carrito (request) :
    return render(request, 'CarritoApp/carrito.html')