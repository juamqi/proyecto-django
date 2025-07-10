from django import forms
from .models import Comentario, Post

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribí tu comentario...'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'categoria']