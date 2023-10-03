from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=50)
    

class ProductoForm(forms.Form):
    nombre    = forms.CharField(max_length=80)
    categoria = forms.CharField(max_length=20)
    precio    = forms.DecimalField(max_digits=19, decimal_places=2 )
    
class BuscaProductoForm(forms.Form):
    nombre    = forms.CharField(max_length=80)
