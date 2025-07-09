from django.shortcuts import render, get_object_or_404
from .models import Post

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')  
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalles_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalles_post.html', {'post': post})