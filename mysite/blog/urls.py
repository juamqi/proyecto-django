from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('post/nuevo/', views.crear_post, name='crear_post'),
    path('post/<int:post_id>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:post_id>/eliminar/', views.eliminar_post, name='eliminar_post'),
]