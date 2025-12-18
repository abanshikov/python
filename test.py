Пусть имеется следующий класс модели:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
И функция представления для отображения текущей записи по слагу:

def post_show_by_slug(request, ps_slug):
    post = # здесь прописывайте функцию get_object_or_404()
    return render(request, 'post/post.html', {'post': post})
Допишите функцию post_show_by_slug для выбора текущей записи поста модели Post по слагу ps_slug с помощью функции get_object_or_404(). Импортировать функции get_object_or_404() и render() не нужно!

P.S. На экран ничего выводить не нужно






from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


def post_show_by_slug(request, ps_slug):
    post = # здесь прописывайте функцию get_object_or_404()
    return render(request, 'post/post.html', {'post': post})