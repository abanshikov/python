Продолжите программу, в которой с помощью декоратора dataclass объявите класс Animal со следующим набором полей (порядок важен):

name (str: имя животного);

old (int: возраст животного);

weight (Any: вес животного).

На основе класса Animal с помощью декоратора dataclass объявите дочерний класс Turtle (черепаха) со следующим набором полей (порядок важен):

weight (float: вес черепахи);

length (float: длина черепахи);

speed (float: скорость черепахи, с исключением из параметров инициализатора и начальным значением 0).

Создайте объект t класса Turtle со следующим набором данных:

name: "Черя"; old: 94; weight: 3.5; length: 108

P.S. На экран ничего выводить не нужно



from dataclasses import dataclass, field
from typing import Any


@dataclass
class Animal:
    name: str
    old: int
    weight: Any


@dataclass
class Turtle(Animal):
    weight: float
    length: float
    speed: float = field(init=False, default=0)


t = Turtle(name="Черя", old=94, weight=3.5, length=108)


print(t)
