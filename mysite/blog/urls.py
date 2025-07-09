from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:post_id>/', views.detalles_post, name='detalles_post'),
    path('accounts/', include('django.contrib.auth.urls')),
]
