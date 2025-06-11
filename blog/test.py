from django.test import TestCase
from .models import Autor, Categoria, Post

class PruebaModeloAutor(TestCase):
    def test_string_representation(self):
        autor = Autor(name="Ros", bio="Bio corta")
        self.assertEqual(str(autor), autor.name)

class PruebaModeloCategoria(TestCase):
    def test_string_representation(self):
        categoria = Categoria(name="Django")
        self.assertEqual(str(categoria), categoria.name)

class PostModelTest(TestCase):
    def test_string_representation(self):
        autor = Autor.objects.create(name="Ros", bio="Bio corta")
        Categoria = Categoria.objects.create(name="Django")
        post = Post.objects.create(title="Mi primera publicación", content="Contenido", autor=autor, categoria=categoria)
        self.assertEqual(str(post), post.title)