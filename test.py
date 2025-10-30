class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        if not isinstance(other, Box):
            raise TypeError("Операнд справа должен иметь тип Box")

        if len(self.things) != len(other.things):
            return False

        things_1 = self.things.copy()
        things_2 = other.things.copy()

        for thing_1 in things_1:
            found = False
            for thing_2 in things_2:
                if thing_1 == thing_2:
                    found = True
                    things_2.remove(thing_2)
                    break
            if not found:
                return False

        return True


class Thing:
    def __init__(self, name: str, mass: (int, float)):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if not isinstance(other, Thing):
            raise TypeError("Операнд справа должен иметь тип Thing")

        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __ne__(self, other):
        if not isinstance(other, Thing):
            raise TypeError("Операнд справа должен иметь тип Thing")

        return self.name.lower() != other.name.lower() and self.mass != other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
