import math

class Triangle:
    def __init__(self, a, b, c):
        self._a = None
        self._b = None
        self._c = None

        # Устанавливаем стороны через свойства для валидации
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle(self.a, self.b, self.c)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

        # После изменения стороны проверяем треугольник
        if self._b is not None and self._c is not None:
            self._validate_triangle(value, self._b, self._c)

        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

        # После изменения стороны проверяем треугольник
        if self._a is not None and self._c is not None:
            self._validate_triangle(self._a, value, self._c)

        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

        # После изменения стороны проверяем треугольник
        if self._a is not None and self._b is not None:
            self._validate_triangle(self._a, self._b, value)

        self._c = value

    @staticmethod
    def _validate_triangle(a, b, c):
        if a is not None and b is not None and c is not None:
            if not (a < b + c and b < a + c and c < a + b):
                raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self._a + self._b + self._c)

    def __call__(self):
        p = (self._a + self._b + self._c) / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
