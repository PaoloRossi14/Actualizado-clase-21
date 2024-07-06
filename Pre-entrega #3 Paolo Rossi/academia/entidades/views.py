from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,"entidades/index.html")

def comprar(request):
    contexto= {"comprar":Compras.objects.all()}
    return render(request,"entidades/comprar.html", contexto)

def projects(request):
    contexto= {"comprar":Visitantes.objects.all()}
    return render(request,"entidades/projects.html", contexto)

def producto(request):
    contexto= {"comprar":Productos.objects.all()}
    return render(request,"entidades/producto.html", contexto)

 # formularios

def comprarFrom(request):
    if request.method =="POST":
        miFrom = comprarFrom(request.POST)
        if miFrom.is_valid():
            comprar_nombre =miFrom.cleaned_data.get("nombre")
            comprar_domicilio=miFrom.cleaned_data.get("domicilio")
            comprar_edad=miFrom.cleaned_data.get("edad")
            comprar_correo=miFrom.cleaned_data.get("correo")
            comprar_telefono=miFrom.cleaned_data.get("telefono")
            comprar_nombredeempresa=miFrom.cleaned_data.get("nombredeempresa")
            comprar = Compras(nombre=comprar_nombre, domicilio= comprar_domicilio, edad=comprar_edad, correo= comprar_correo, telefono= comprar_telefono, nombredeempresa=comprar_nombredeempresa)
            comprar.save()
            contexto = {"comprar": Compras.objects.all()}
            return render(request,"entidades/comprar.html", contexto)
    else:
        miFrom = ComprasFrom()
    return render(request, "entidad/comprarForm.html", {"Form": miFrom})


def productosFrom(request):
    if request.method =="POST":
        miFrom = ProductosFrom(request.POST)
        if miFrom.is_valid():
            productos_nombre =miFrom.cleaned_data.get("nombre")
            productos_precio=miFrom.cleaned_data.get("precio")
            productos_stock=miFrom.cleaned_data.get("stock")
            productos = Productos(nombre=productos_nombre, precio= productos_precio, stock= productos_stock)
            productos.save()
            contexto = {"productos": Productos.objects.all()}
            return render(request,"entidades/productos.html", contexto)
    else:
        miFrom = ProductosFrom()
    return render(request, "entidad/productosForm.html", {"Form": miFrom})

 
def buscarCompras(request):
    return render(request, "entidades/buscar.html")

def encontrarCompras(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        comprar=Compras.objects.filter(nombre__icontains=patron)
        contexto= {'comprar': comprar}
    else:
        contexto={'comprar': Compras.objects.all()}
    return render(request, "entidades/comprar.html")