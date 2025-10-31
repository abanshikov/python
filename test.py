l_inp = s_inp.split(";")


class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __setattr__(self, key, value):
        if value  <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, key, value)

    def __str__(self):
        return f"a={self.a} b={self.b} c={self.c}"

    def __repr__(self):
        return f"a={self.a} b={self.b} c={self.c}"


lst_dims = []
for string in l_inp:
    a, b, c = (float(_) for _ in string.split())
    lst_dims.append(Dimensions(a, b, c))

# print(lst_dims)

lst_dims.sort(key=lambda x: hash(x))
# print(lst_dims)
