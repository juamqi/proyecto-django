from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def app_rutina_home(request):
    return redirect('app_rutina/login/')

urlpatterns = [
]