from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "MiApp/index.html")


def cliente(request):
    return HttpResponse("alta cliente!")

def producto(request):
    return HttpResponse("alta peoducto!")

def orden(request):
    return HttpResponse("alta orden!")
