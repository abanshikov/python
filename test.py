from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        if not (a < b+c and b < a+c and c < a+b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    def __setattr__(self, key, value):
        if value  <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        object.__setattr__(self, key, value)

    def __len__(self):
        return int(self.__a + self.__b + self.__c)

    def tr(self):
        p = len(self)
        return sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
