from django.shortcuts import render
from django.http      import HttpResponse
from MiApp.forms      import ClienteForm, ProductoForm, BuscaProductoForm
from .models          import Clientes, Productos

# Create your views here.

def inicio(request):
    if request.method == "GET":
        mis_productos = Productos.objects.all()
    #return render(request, "MiApp/index.html")
    return render(request, "MiApp/resultados.html", {"productos":mis_productos})

def orden(request):
    return HttpResponse("alta orden!")


def cliente (request) :
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
    
        if miForm.is_valid():
            datos = miForm.cleaned_data
            cliente = Clientes(nombre=datos["nombre"], email=datos["email"])
            cliente.save()
            mis_productos = Productos.objects.all()
            return render(request, "MiApp/resultados.html", {"productos":mis_productos})
            #return render(request, "MiApp/index.html")
    else:
        miForm = ClienteForm()

    return render(request, "MiApp/form_api.html", {"miForm": miForm}) 


def producto (request) :
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
    
        if miForm.is_valid():
            datos = miForm.cleaned_data
            producto = Productos(nombre=datos["nombre"], categoria=datos["categoria"], precio=datos["precio"])
            producto.save()
            mis_productos = Productos.objects.all()
            return render(request, "MiApp/resultados.html", {"productos":mis_productos})
            #return render(request, "MiApp/index.html")
    else:
        miForm = ProductoForm()

    return render(request, "MiApp/form_api.html", {"miForm": miForm}) 


def buscoproducto(request):
    if request.method == "POST":
        miForm = BuscaProductoForm(request.POST) 
        
        if miForm.is_valid():
            dato = miForm.cleaned_data
            
            mis_productos = Productos.objects.filter(nombre__icontains=dato["nombre"])
            return render(request, "MiApp/resultados.html", {"productos":mis_productos})
    else:
        miForm = BuscaProductoForm()

    return render(request, "MiApp/form_api.html", {"miForm": miForm})


def mostrarproducto(request):
    return HttpResponse("mostrando!")
