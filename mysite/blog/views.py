from django.shortcuts import render
from .models import Post

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')  
    return render(request, 'blog/lista_posts.html', {'posts': posts})