lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


lst_in = list(map(str.strip, sys.stdin.readlines()))
##lst_in = ['Системный блок: 1500 75890.56',
##          'Монитор Samsung: 2000 34000',
##          'Клавиатура: 200.44 545',
##          'Монитор Samsung: 2000 34000']

shop_items = {}
items = []
for string in lst_in:
    name = string.split(":")[0]
    weight, price = (float(x) for x in string.split(":")[1].split())

    item = ShopItem(name, weight, price)
    count_of_item = items.count(item) + 1

    shop_items[item] = [item, count_of_item]
    items.append(item)

##print(shop_items)
