from django.urls import path
from ProyectoFinalApp.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login', login_request, name='login'),
    path('registro', registro, name='registro'),
    path('logout', logout_request, name='logout')
]
