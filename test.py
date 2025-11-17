def input_int_numbers():
    try:
        return tuple(map(int, input().split()))
    except:
        raise TypeError('все числа должны быть целыми')


while True:
    try:
        a = input_int_numbers()
        break
    except:
        pass


print(*a)
