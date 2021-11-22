class ItemDiscount:

    def __init__(self, name, price):
        self.price = price
        self.name = name

    def modify_price(self, new_price):
        self.price = new_price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return f"{self.name} {self.price - self.price / 100 * self.discount}"

    def get_info(self):
        return f"{self.name} {self.price}"


item = ItemDiscountReport('Volvo', 6000000, 10)
print(item)
item.modify_price(8000000)
print(item)
