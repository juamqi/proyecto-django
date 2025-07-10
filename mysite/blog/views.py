from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import ComentarioForm, PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required

def lista_posts(request):
    categoria = request.GET.get('categoria')
    anio = request.GET.get('anio')
    min_comentarios = request.GET.get('comentarios')

    posts = Post.objects.all()

    if categoria:
        posts = posts.filter(categoria=categoria)

    if anio:
        posts = posts.filter(fecha_publicacion__year=anio)

    posts = posts.annotate(num_comentarios=Count('comentarios'))

    if min_comentarios:
        posts = posts.filter(num_comentarios__gte=min_comentarios)

    posts = posts.order_by('-fecha_publicacion')

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

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) 
            return redirect('lista_posts')  
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            nuevo_post = form.save(commit=False)
            nuevo_post.autor = request.user.username
            nuevo_post.save()
            return redirect('detalle_post', post_id=nuevo_post.id)
    else:
        form = PostForm()
    
    return render(request, 'blog/crear_post.html', {'form': form})

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.autor != request.user.username:
        return redirect('lista_posts') 

    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('detalle_post', post_id=post.id)

    return render(request, 'blog/editar_post.html', {'form': form, 'post': post})

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.autor != request.user.username:
        return redirect('lista_posts')

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')

    return render(request, 'blog/eliminar_post.html', {'post': post})