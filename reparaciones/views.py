from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Tecnico, Usuario
from django.http import HttpResponse
from django.contrib.auth.models import Group

def inicio(request):
    query_set = Group.objects.filter(user = request.user)
    for g in query_set:
        if g.name == "Tecnico":
            context = {}
            return render(request, 'home/pagina_principal_tecnico.html', context)
        else:
            context = {}
            return render(request, 'home/pagina_principal_usuario.html', context)
    # return HttpResponse('<h1>{{ user_auth }}</h1>')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Intenta autenticar al usuario como Tecnico o Usuario
        user = authenticate(request, alias_tecnico=username, contra_tecnico=password) or \
               authenticate(request, alias_usuario=username, contra_usuario=password)
        
        if user is not None:
            # Iniciar sesión
            login(request, user)
            if user.tipo == 'tecnico':
                return redirect('pagina_principal_tecnico')
            elif user.tipo == 'usuario':
                return redirect('pagina_principal_usuario')

        # Lógica para manejar un intento fallido de inicio de sesión
        pass

    return render(request, 'login/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def pagina_principal_usuario(request):
    context = {}
    return render(request, 'home/pagina_principal_usuario.html', context)

@login_required
def pagina_principal_tecnico(request):
    context = {}
    return render(request, 'home/pagina_principal_tecnico.html', context)
    