class ListInteger(list):
    @staticmethod
    def __is_int(x):
        if type(x) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, lst):
        for l in lst:
            self.__is_int(l)
        super().__init__(lst)

    def __setitem__(self, key, value):
        self.__is_int(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.__is_int(value)
        super().append(value)


##s = ListInteger((1, 2, 3))
##s[1] = 10
##s.append(11)
##print(s)
##s[0] = 10.5 # TypeError
