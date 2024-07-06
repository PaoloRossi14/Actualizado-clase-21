from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', home, name="home"),
    path('comprar/', comprar, name="comprar"),
    path('projects/', projects, name="projects"),
    path('producto/', producto, name="producto"),
    path('admin/', home, name="home"),
    path('', home, name="home"),
    path('comprarForm/', comprarFrom, name="comprarForm"),
    path('productosForm/', productosFrom, name="productosForm"),
    path('buscarCompras/', buscarCompras, name="buscarCompras"),
        path('encontrarCompras/', encontrarCompras, name="encontrarCompras"),
]
