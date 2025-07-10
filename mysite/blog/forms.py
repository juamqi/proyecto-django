from django import forms
from .models import Comentario, Post, Categoria

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        sin_cat = Categoria.objects.filter(nombre="Sin categoría")
        otras = Categoria.objects.exclude(nombre="Sin categoría").order_by('nombre')
        self.fields['categoria'].queryset = sin_cat | otras