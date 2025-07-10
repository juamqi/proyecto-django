from django.contrib import admin
from .models import Ejercicio, Rutina, DiaRutina, EjercicioDia, Progreso

admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(DiaRutina)
admin.site.register(EjercicioDia)
admin.site.register(Progreso)