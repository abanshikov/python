from random import randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length= max_length

    def __call__(self, *args, **kwargs):
        psw = ""
        for i in range(self.__min_length, randint(self.__min_length+1, self.__max_length)):
            psw += self.__psw_chars[randint(0, len(self.__psw_chars)-1)]

        return psw

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
psw = rnd()

lst_pass = [rnd() for i in range(3)]
