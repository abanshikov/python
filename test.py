class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro: (int, float) = ro
        self.volume: (int, float) = volume
        self.m: (int, float) = ro * volume

    def __eq__(self, other):
        if not isinstance(other, Body):
            raise TypeError("Операнд справа должен иметь тип числа или Body")

        m = other if isinstance(other, (int, float)) else other.m
        return self.m == m

    def __gt__(self, other):
        if not isinstance(other, Body):
            raise TypeError("Операнд справа должен иметь тип Body")

        return self.m > other.m

    def __lt__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Операнд справа должен иметь тип int или float")

        return self.m < other
