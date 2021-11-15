class ItemDiscount:

    def __init__(self, name, price):
        self.price = price
        self.name = name

    def modify_price(self, new_price):
        self.price = new_price


class ItemDiscountReport(ItemDiscount):

    def get_info(self):
        return f"{self.name} {self.price}"


item = ItemDiscountReport('Volvo', 6000000)
print(item.get_info())
item.modify_price(8000000)
print(item.get_info())
