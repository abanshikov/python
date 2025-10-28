import sys

# здесь пишите программу

lst_in = list(map(str.strip, sys.stdin.readlines()))



class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.__title: str = title
        self.__author: str = author
        self.__pages: int = pages

    def __str__(self):
        return f"Книга: {self.__title}; {self.__author}; {self.__pages}"


book = Book(lst_in[0], lst_in[1], lst_in[2])
