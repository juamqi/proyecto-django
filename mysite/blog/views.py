from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import ComentarioForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')  
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentarios.all().order_by('-fecha')
    nuevo_comentario = None

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                nuevo_comentario = form.save(commit=False)
                nuevo_comentario.post = post
                nuevo_comentario.autor = request.user
                nuevo_comentario.save()
                form = ComentarioForm()  
        else:
            form = ComentarioForm() 
    else:
        form = ComentarioForm()

    return render(request, 'blog/detalle_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
        'nuevo_comentario': nuevo_comentario
    })