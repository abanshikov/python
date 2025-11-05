class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __str__(self):
        return f"name: {self.name} price: {self.price} weight: {self.weight}"


class DictShop(dict):
    def __init__(self, things=None):
        things = {} if things is None else things

        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        if things and all(isinstance(key, Thing) for key in things):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__init__(things)

    def __setitem__(self, key, value):
        if type(key) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)
