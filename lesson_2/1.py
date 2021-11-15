class ItemDiscount:

    def __init__(self, name, price):
        self.price = price
        self.name = name


class ItemDiscountReport(ItemDiscount):

    def get_info(self):
        return f"{self.name} {self.price}"


item = ItemDiscountReport('Volvo', 6000000)
print(item.get_info())
