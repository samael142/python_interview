class ItemDiscount:

    def __init__(self, name, price):
        self.__price = price
        self.__name = name

    def get_parent_info(self):
        return f"{self.__name} {self.__price}"


class ItemDiscountReport(ItemDiscount):

    def get_info(self):
        return f"{self.__name} {self.__price}"


item = ItemDiscountReport('Volvo', 6000000)
print(item.get_parent_info())
