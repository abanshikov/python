Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
Используя метод filter() стандартного менеджера записей класса Person, выберите все записи с параметром job равным "Программист".

P.S. На экран ничего выводить не нужно