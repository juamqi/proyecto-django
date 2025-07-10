from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORIAS = [
        ('TEC', 'Tecnología'),
        ('VID', 'Vida'),
        ('ART', 'Arte'),
        ('OTR', 'Otra'),
    ]
    
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=3, choices=CATEGORIAS, default='OTR')

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username} - {self.post.titulo}'