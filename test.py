С помощью декоратора dataclass:

from dataclasses import dataclass
объявите Data Class с именем Volume без добавления инициализатора и метода __repr__ и со следующим набором полей (порядок важен):

height (int: высота);
width (int: ширина);
depth (int: глубина).
Также в классе Volume объявите метод get_volume, который бы возвращал объем, вычисленный по формуле:

V=height⋅width ⋅depth

Создайте объект с именем v класса Volume. Задайте значения локальных атрибутов height, width, depth объекта v значениями 10, 20, 30 соответственно. Вызовите метод get_volume для объекта v и результат сохраните в переменной res.

P.S. На экран ничего выводить не нужно



from dataclasses import dataclass


@dataclass(init=False, repr=False)
class Volume:
    height: int
    width: int
    depth: int

    def get_volume(self):
        return self.height * self.width * self.depth


v = Volume()
v.height = 10
v.width = 20
v.depth = 30

res = v.get_volume()
