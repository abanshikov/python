from django.db import models


class ShopItem(models.Model):
    name = models.CharField(max_lenght=100)
    weight = models.IntegerField(default=0, block=True)
    price = models.IntegerField(default=0)
    is_exists = models.BooleanField(default=True)


records = ShopItem().objects.all()
