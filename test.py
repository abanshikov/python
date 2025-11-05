class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

class Plants(Protists):
    def __init__(self, *args):
        super().__init__(*args)

class Animals(Protists):
    def __init__(self, *args):
        super().__init__(*args)

class Mosses(Plants):
    def __init__(self, *args):
        super().__init__(*args)

class Flowering(Plants):
    def __init__(self, *args):
        super().__init__(*args)

class Worms(Animals):
    def __init__(self, *args):
        super().__init__(*args)

class Mammals(Animals):
    def __init__(self, *args):
        super().__init__(*args)

class Human(Mammals):
    def __init__(self, *args):
        super().__init__(*args)

class Monkeys(Mammals):
    def __init__(self, *args):
        super().__init__(*args)

class Monkey(Monkeys):
    def __init__(self, *args):
        super().__init__(*args)

class Person(Human):
    def __init__(self, *args):
        super().__init__(*args)

class Flower(Flowering):
    def __init__(self, *args):
        super().__init__(*args)

class Worm(Worms):
    def __init__(self, *args):
        super().__init__(*args)


lst_objs = list()
lst_objs.append(Monkey("мартышка", 30.4, 7))
lst_objs.append(Monkey("шимпанзе", 24.6, 8))
lst_objs.append(Person("Балакирев", 88, 34))
lst_objs.append(Person("Верховный жрец", 67.5, 45))
lst_objs.append(Flower("Тюльпан", 0.2, 1))
lst_objs.append(Flower("Роза", 0.1, 2))
lst_objs.append(Worm("червь", 0.01, 1))
lst_objs.append(Worm("червь 2", 0.02, 1))

lst_animals = [item for item in lst_objs if isinstance(item, Animals)]
lst_plants = [item for item in lst_objs if isinstance(item, Plants)]
lst_mammals = [item for item in lst_objs if isinstance(item, Mammals)]
