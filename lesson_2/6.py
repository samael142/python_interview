class ItemDiscount:

    def __init__(self, name, price):
        self.price = price
        self.name = name

    def modify_price(self, new_price):
        self.price = new_price


class ItemNameReport(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return self.name

    def get_info(self):
        return print(self.name)


class ItemPriceReport(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return self.price - self.price / 100 * self.discount

    def get_info(self):
        return print(self.price)


item_1 = ItemNameReport('Volvo', 6000000)
item_2 = ItemPriceReport('Audi', 8000000)

item_1.get_info()
item_2.get_info()


def obj_handler(obj):
    obj.get_info()


obj_handler(item_1)
obj_handler(item_2)

for obj in (item_1, item_2):
    obj.get_info()
