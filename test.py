Пусть имеется следующий класс формы:

# --------------- forms.py -------------------------
from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import AddPostForm

# здесь продолжайте программу
Объявите функцию представления с именем post_new, в которой:

при POST-запросе формируется заполненная форма AddPostForm; выполняется проверка корректности данных формы; если данные корректны, то возвращается объект формы;
при GET-запросе создается пустая форма AddPostForm; с помощью функции render формируется HTML-документ по шаблону 'women/addpage.html' с передачей в него объекта формы AddPostForm через переменную (ключ) form.
P.S. На экран ничего выводить не нужно