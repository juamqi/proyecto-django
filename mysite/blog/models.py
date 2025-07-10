from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

def get_categoria_default():
    return Categoria.objects.get(nombre="Sin categoría").id

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_DEFAULT,
        default=5,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username} - {self.post.titulo}'