from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def inicio(request):
    dia_actual = datetime.datetime.now().strftime('%A')  
    rutinas = []  
    ejercicios_de_hoy = []
    context = {
        'dia_actual': dia_actual,
        'rutinas': rutinas,
        'ejercicios_de_hoy': ejercicios_de_hoy,
    }
    return render(request, 'inicio.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) 
            return redirect('inicio')  
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')