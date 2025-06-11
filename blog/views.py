from django.shortcuts import render, redirect
from .models import Post, Autor, Categoria
from .forms import PostForm, AutorForm, CategoriaForm, PostBusquedaForm

def home(request):
    return render(request, 'blog/home.html')

def post_lista(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_lista.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_lista')
    else:
        form = PostForm()
    return render(request, 'blog/post_formulario.html', {'form': form})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'blog/autor_formulario.html', {'form': form})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria_formulario.html', {'form': form})

def post_busqueda(request):
    results = []
    if request.method == 'POST':
        form = PostBusquedaForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(titulo__icontains=query)
    else:
        form = PostBusquedaForm()
    return render(request, 'blog/post_busqueda.html', {'form': form, 'resultados': results})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/lista_autores.html', {'autores': autores})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista_categorias.html', {'categorias': categorias})