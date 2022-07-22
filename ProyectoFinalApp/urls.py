from django.urls import path
from ProyectoFinalApp.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login', login_request, name='login'),
    path('registro', registro, name='registro'),
    path('logout', logout_request, name='logout'),
    path('editar-perfil', editarPerfil, name='editar perfil'),
    path('agregar-avatar', aregarAvatar, name='agregar avatar'),
    path('enviar-mensaje', enviarMensaje, name='enviar mensaje'),
    path('bandeja-entrada', bandejaEntrada, name='bandeja de entrada'),
]
