from django.db import models

# Create your models here.
class Compras(models.Model):
    nombre= models.CharField(max_length=50)
    domicilio=models.CharField(max_length=50)
    edad=models.IntegerField()
    correo=models.CharField(max_length=50)
    telefono=models.IntegerField()
    nombredeempresa=models.CharField(max_length=50)


class Visitantes(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email=models.EmailField()

class Productos(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    stock= models.IntegerField()
