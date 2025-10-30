class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    @classmethod
    def __check_value(cls, x):
        return cls.MIN_DIMENSION <= x <= cls.MAX_DIMENSION

    def __init__(self, a, b, c):
        self.__a = a if self.__check_value(a) else 0
        self.__b = b if self.__check_value(b) else 0
        self.__c = c if self.__check_value(c) else 0

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__check_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @a.setter
    def b(self, value):
        if self.__check_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @a.setter
    def c(self, value):
        if self.__check_value(value):
            self.__c = value

    def __ge__(self, dim):
        if not isinstance(dim, Dimensions):
            raise TypeError("Операнд справа должен иметь тип Dimensions")

        return self.volume() >= dim.a * dim.b * dim.c

    def __gt__(self, dim):
        if not isinstance(dim, Dimensions):
            raise TypeError("Операнд справа должен иметь тип Dimensions")

        return self.volume() > dim.a * dim.b * dim.c

    def __le__(self, dim):
        if not isinstance(dim, Dimensions):
            raise TypeError("Операнд справа должен иметь тип Dimensions")

        return self.volume() <= dim.a * dim.b * dim.c

    def __lt__(self, dim):
        if not isinstance(dim, Dimensions):
            raise TypeError("Операнд справа должен иметь тип Dimensions")

        return self.volume() < dim.a * dim.b * dim.c

    def volume(self):
        return self.__a * self.__b * self.__c


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [
        ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
        ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
        ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
        ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)),
        ]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
