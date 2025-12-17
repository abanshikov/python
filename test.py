from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=100)  # строка с максимальной длиной 100 символов; обязательное поле;
    model = models.CharField()  # марка машины; обязательное поле;
    price = models.IntegerField(default=0, blank=True)  # цена машины с начальным значением 0; необязательное поле;
    is_exists = models.BooleanField(default=True)  # наличие товара (True - присутствует; False - отсутствует); по умолчанию True.


Auto.objects.create(name="BMW X6", model="BMW", price=6000111)
Auto.objects.create(name="Toyota Corolla", model="Toyota")
Auto.objects.create(name="Haval 7", model="Haval", price=3500222)


autos = Auto.objects.all()[0]
