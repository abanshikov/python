from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.__coords = [0] * args[0]
        else:
            self.__coords = args

    def set_coords(self, *args):
        for i in range(min(len(args), len(self.__coords))):
            self.__coords[i] = float(args[i])

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sqrt(sum([x**2 for x in self.__coords]))
