from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pkg_resources import require
from ProyectoFinalApp.models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', max_length=100, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        
class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Usuario', max_length=100, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        
class AvatarForm(UserCreationForm):
    imagen = forms.ImageField(label='Imagen', required=False)
    bio = forms.CharField(label = 'Bio', required = False)
    class Meta:
        model = Avatar
        fields = ['bio', 'imagen']
        
class CrearMensajeForm(forms.Form):
    destinatario = forms.EmailField(label='Email', required=True, 
                                    widget=forms.Select(choices=[('', 'Seleccione un destinatario')] + 
                                    [(user.email, user.email) for user in User.objects.all()]))
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea)
    