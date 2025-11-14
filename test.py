В программе ниже объявлен класс Thing следующим образом:

from dataclasses import dataclass
from typing import Any


@dataclass
class Thing:
    name: Any
    color: Any
    weight: float
Необходимо продолжить эту программу и объявить дочерний класс Table от базового класса Thing, как Data Class, используя декоратор dataclass. Дочерний класс Table должен иметь следующие поля (порядок важен):

width (float: ширина стола);
height (float: высота стола).
Создайте объект tb класса Table со следующим набором данных:

name: "Suprise"; color: "red"; weight: 102.5; width: 0.45; height: 10.1

P.S. На экран ничего выводить не нужно



from dataclasses import dataclass
from typing import Any


@dataclass
class Thing:
    name: Any
    color: Any
    weight: float


@dataclass
class Table(Thing):
    width: float
    height: float


tb = Table(name="Suprise", color="red", weight=102.5, width=0.45, height=10.1)


print(tb)
