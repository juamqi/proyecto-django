from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ejercicios/', views.lista_ejercicios, name='lista_ejercicios'),
    path('ejercicios/crear/', views.ejercicio_crear, name='ejercicio_crear'),
    path('ejercicios/<int:pk>/', views.ejercicio_detalle, name='ejercicio_detalle'),
    path('ejercicios/<int:pk>/editar/', views.ejercicio_editar, name='ejercicio_editar'),
    path('ejercicios/<int:pk>/eliminar/', views.ejercicio_eliminar, name='ejercicio_eliminar'),
]