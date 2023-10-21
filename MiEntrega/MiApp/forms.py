from django                      import forms
from django.contrib.auth.forms   import UserCreationForm
from django.contrib.auth.models  import User


class ProductoForm(forms.Form):
    nombre    = forms.CharField(max_length=80)
    categoria = forms.CharField(max_length=20)
    precio    = forms.DecimalField(max_digits=19, decimal_places=2 )
    
class BuscaProductoForm(forms.Form):
    nombre    = forms.CharField(max_length=80)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        #help_text = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, required=False)

    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password1', 'password2']
        