from django import forms

class ComprasFrom(forms. From):
    nombre= forms.CharField (max_length=50, required=True)
    domicilio= forms.CharField(max_length=50, required=True)
    edad= forms.IntegerField(required=True)
    correo= forms.CharField(max_length=50, required=True)
    telefono= forms.IntegerField(required=True)
    nombredeempresa= forms.CharField(max_length=50, required=True)

class ProductosFrom(forms. From):
    nombre= forms.CharField (max_length=50, required=True)
    precio= forms.IntegerField(required=True)
    stock= forms.IntegerField(required=True)