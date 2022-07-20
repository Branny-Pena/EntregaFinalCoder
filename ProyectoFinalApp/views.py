import django
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from ProyectoFinalApp.forms import UserRegisterForm
from ProyectoFinalApp.models import perfil

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
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'ProyectoFinalApp\inicio.html', {'mensaje':'Usuario creado'}) 
    else:
        form = UserRegisterForm()
        
    
    return render(request, r'ProyectoFinalApp\registro.html', {'form':form})

def logout_request(request):
    logout(request)
    return redirect('inicio')