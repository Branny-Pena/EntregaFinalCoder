import django
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from ProyectoFinalApp.forms import *
from ProyectoFinalApp.models import Perfil

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def inicio(request):
    return render(request, 'ProyectoFinalApp\inicio.html', {})

def informacion(request):
    return render(request, 'ProyectoFinalApp\informacion.html', {})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                return render(request, 'ProyectoFinalApp\inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            
            else:
                return render(request, 'ProyectoFinalApp\inicio.html', {'mensaje': 'Error, datos incorrectos'})
            
        else:
            return render(request, 'ProyectoFinalApp\inicio.html', {'mensaje': 'Error, formulario incorrecto'})
    
    form = AuthenticationForm()
    return render(request, 'ProyectoFinalApp\login.html', {'form':form})
    

def registro(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            informacion = form.cleaned_data
            username = informacion.get('username')
            password = informacion.get('password1')
            
            form.save()
            
            user_auth = authenticate(username=username, password=password)
            
            if username is not None:
                login(request, username)
                return redirect('inicio')
            else:
                return redirect('login')
            
        return render(request, r'ProyectoFinalApp\registro.html', {'form':form})
    
    form = UserRegisterForm()

    return render(request, r'ProyectoFinalApp\registro.html', {'form':form})

def logout_request(request):
    logout(request)
    return redirect('inicio')

@login_required
def editarPerfil(request):
    
    user = request.user
    
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.email = informacion['email']
            user.save()
            return redirect('inicio')
        else:
            form = UserEditForm(initial={"email":user.email})
        
        return render(request, 'ProyectoFinalApp\editar-perfil.html')


