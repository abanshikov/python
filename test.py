class PrimaryKeyError(Exception):
    def __init__(self, id = None, pk = None):
        if id:
            self.message = f"Значение первичного ключа id = {id} недопустимо"
        elif pk:
            self.message = f"Значение первичного ключа pk = {pk} недопустимо"
        else:
            self.message = "Первичный ключ должен быть целым неотрицательным числом"

    def __str__(self):
        return self.message


e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо


print(e2) # Значение первичного ключа id = abc недопустимо


try:
    e2 = PrimaryKeyError(id=-10.5)
    raise e2
except PrimaryKeyError:
    print(e2)
