from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from .models import Ejercicio
from django.db.models import Q

def inicio(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'inicio.html')

@login_required
def dashboard(request):
    dia_actual = datetime.datetime.now().strftime('%A')  
    rutinas = []  
    ejercicios_de_hoy = []
    context = {
        'dia_actual': dia_actual,
        'rutinas': rutinas,
        'ejercicios_de_hoy': ejercicios_de_hoy,
    }
    return render(request, 'dashboard.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) 
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')

@login_required
def lista_ejercicios(request):
    ejercicios = Ejercicio.objects.all()
    
    buscar = request.GET.get('buscar')
    if buscar:
        ejercicios = ejercicios.filter(
            Q(nombre__icontains=buscar) | 
            Q(descripcion__icontains=buscar)
        )
    
    grupo_muscular = request.GET.get('grupo_muscular')
    if grupo_muscular:
        ejercicios = ejercicios.filter(grupo_muscular=grupo_muscular)
    
    tipo = request.GET.get('tipo')
    if tipo == 'predefinido':
        ejercicios = ejercicios.filter(creado_por_usuario=False)
    elif tipo == 'personalizado':
        ejercicios = ejercicios.filter(creado_por_usuario=True, usuario=request.user)
    
    ejercicios = ejercicios.filter(
        Q(creado_por_usuario=False) | 
        Q(creado_por_usuario=True, usuario=request.user)
    )
    
    context = {
        'ejercicios': ejercicios,
    }
    return render(request, 'ejercicios/lista_ejercicios.html', context)

@login_required
def ejercicio_detalle(request, pk):
    ejercicio = get_object_or_404(Ejercicio, pk=pk)
    
    if ejercicio.creado_por_usuario and ejercicio.usuario != request.user:
        messages.error(request, 'No tienes permisos para ver este ejercicio.')
        return redirect('lista_ejercicios')
    
    context = {
        'ejercicio': ejercicio,
    }
    return render(request, 'ejercicios/detalle_ejercicio.html', context)

@login_required
def ejercicio_crear(request):
    if request.method == 'POST':
        messages.success(request, 'Función de crear ejercicio en desarrollo.')
        return redirect('lista_ejercicios')
    
    messages.info(request, 'Función de crear ejercicio en desarrollo.')
    return redirect('lista_ejercicios')

@login_required
def ejercicio_editar(request, pk):
    ejercicio = get_object_or_404(Ejercicio, pk=pk)
    
    if not ejercicio.creado_por_usuario or ejercicio.usuario != request.user:
        messages.error(request, 'No tienes permisos para editar este ejercicio.')
        return redirect('lista_ejercicios')
    
    if request.method == 'POST':
        messages.success(request, 'Función de editar ejercicio en desarrollo.')
        return redirect('lista_ejercicios')
    
    messages.info(request, 'Función de editar ejercicio en desarrollo.')
    return redirect('lista_ejercicios')

@login_required
def ejercicio_eliminar(request, pk):
    ejercicio = get_object_or_404(Ejercicio, pk=pk)
    
    if not ejercicio.creado_por_usuario or ejercicio.usuario != request.user:
        messages.error(request, 'No tienes permisos para eliminar este ejercicio.')
        return redirect('lista_ejercicios')
    
    if request.method == 'POST':
        messages.success(request, 'Función de eliminar ejercicio en desarrollo.')
        return redirect('lista_ejercicios')
    
    messages.info(request, 'Función de eliminar ejercicio en desarrollo.')
    return redirect('lista_ejercicios')