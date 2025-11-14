В программе ниже объявлен класс Table следующим образом:

@dataclass
class Table:
    current_id = 0
    id: int = field(init=False, compare=False, default=-1)
    model: str
    color: Any

    def __post_init__(self):
        Table.current_id += 1
        self.id = Table.current_id
Необходимо продолжить эту программу и объявить дочерний класс RoundTable от базового класса Table, как Data Class, используя декоратор dataclass. Дочерний класс RoundTable должен содержать следующие поля (порядок важен):

radius (InitVar с типом int: радиус столешницы);
height (int: высота стола).
square (float: площадь столешницы; с исключением из параметров инициализатора и операций сравнения).
Объявите метод __post_init__ в классе RoundTable, в котором выполните расчет площади столешницы по формуле:

S=3.1415⋅radius 
2
 

с сохранением результата в локальном атрибуте self.square. При реализации метода __post_init__ следует учесть вызов такого же метода базового класса.

Создайте объект rt класса RoundTable со следующим набором данных:

model: "RT"; color: "green"; radius: 120; height: 90

P.S. На экран ничего выводить не нужно.


rt = RoundTable("RT", "green", 120, 90)