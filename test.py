class Tuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return Tuple(super().__add__(tuple(other)))
        return NotImplemented

    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            return Tuple(tuple(other) + super().__add__(tuple()))
        return NotImplemented
