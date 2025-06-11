from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_lista', views.post_lista, name='post_lista'),
    path('post_nuevo', views.post_create, name='post_nuevo'),
    path('autor_nuevo', views.autor_create, name='autor_nuevo'),
    path('categoria_nueva', views.categoria_create, name='categoria_nueva'),
    path('posts_busqueda', views.post_busqueda, name='post_busqueda'),
    path('lista_autores', views.lista_autores, name='lista_autores'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
]