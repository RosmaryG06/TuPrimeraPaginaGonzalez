from django import forms
from .models import Post, Autor, Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name', 'bio']
        labels = {'name': 'Nombre',
                  'bio': 'Bibliografía'}

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']
        labels = {'name': 'Nombre'}

class PostBusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar por título', max_length=200)