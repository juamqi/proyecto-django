from django.db import models
from django.contrib.auth.models import User

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='ejercicios/imagenes/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    creado_por_usuario = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
    
    def __str__(self):
        return self.nombre

class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"

class DiaRutina(models.Model):
    DIAS_SEMANA = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miércoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sábado'),
        ('DO', 'Domingo'),
    ]
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='dias')
    dia_semana = models.CharField(max_length=2, choices=DIAS_SEMANA)

    class Meta:
        verbose_name = "Día de Rutina"
        verbose_name_plural = "Días de Rutina"

    def __str__(self):
        return f"{self.get_dia_semana_display()} - {self.rutina.nombre}"


class EjercicioDia(models.Model):
    dia_rutina = models.ForeignKey(DiaRutina, on_delete=models.CASCADE, related_name='ejercicios')
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    series = models.PositiveIntegerField()
    repeticiones = models.PositiveIntegerField()
    peso_sugerido = models.FloatField(blank=True, null=True)
    orden = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Ejercicio por Día"
        verbose_name_plural = "Ejercicios por Día"
        ordering = ['orden']

    def __str__(self):
        return f"{self.ejercicio.nombre} - {self.dia_rutina}"


class Progreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rutina = models.ForeignKey(Rutina, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    series_realizadas = models.PositiveIntegerField()
    reps_realizadas = models.PositiveIntegerField()
    peso_usado = models.FloatField(blank=True, null=True)
    comentarios = models.TextField(blank=True)

    class Meta:
        verbose_name = "Progreso"
        verbose_name_plural = "Progresos"

    def __str__(self):
        return f"{self.usuario.username} - {self.ejercicio.nombre} ({self.fecha})"