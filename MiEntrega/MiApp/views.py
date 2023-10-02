from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "MiApp/index.html")


def cliente(request):
    return render(request, "MiApp/cliente.html")

def producto(request):
    return render(request, "MiApp/producto.html")

def orden(request):
    return HttpResponse("alta orden!")
