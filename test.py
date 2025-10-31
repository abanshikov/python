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
        self._validate_triangle()
    
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        self._a = value
        # После изменения стороны проверяем треугольник
        if self._b is not None and self._c is not None:
            self._validate_triangle()
    
    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        self._b = value
        # После изменения стороны проверяем треугольник
        if self._a is not None and self._c is not None:
            self._validate_triangle()
    
    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        self._c = value
        # После изменения стороны проверяем треугольник
        if self._a is not None and self._b is not None:
            self._validate_triangle()
    
    def _validate_triangle(self):
        if self._a is not None and self._b is not None and self._c is not None:
            if not (self._a < self._b + self._c and 
                    self._b < self._a + self._c and 
                    self._c < self._a + self._b):
                raise ValueError("с указанными длинами нельзя образовать треугольник")
    
    def __len__(self):
        return int(self._a + self._b + self._c)
    
    def __call__(self):
        p = (self._a + self._b + self._c) / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))