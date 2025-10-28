from math import sqrt


class Complex:
    def __init__(self, real: (int, float), img: (int, float)):
        self.__real = real
        self.__img = img

    def __setattr__(self, key, value):
        if key in ("rear", "img") and type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        object.__setattr__(self, key, value)

    def __abs__(self):
        return sqrt(self.real**2 + self.img**2)

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value


cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.imp = 4
c_abs = abs(cmp)
