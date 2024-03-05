from src.abstract_product import AbstractProduct
from src.mixin_log import MixinLog


class Product(AbstractProduct, MixinLog):
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int, colour: str = None):
        self.name: str = name
        self.description: str = description
        self._price: float = price
        self.quantity_in_stock: int = quantity_in_stock
        self.colour = colour
        super().__init__()

    @classmethod
    def create_and_return_product(cls, name: str, description: str, price: float, quantity_in_stock: int):
        return cls(name, description, price, quantity_in_stock)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена не корректно")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        if type(other) is type(self):

            if other.quantity_in_stock < 1:
                raise ValueError('Количество добавляемого товара меньше 1')

            pt_summ = self.quantity_in_stock * self._price + other.quantity_in_stock * other.price
            return pt_summ
        else:
            raise TypeError
