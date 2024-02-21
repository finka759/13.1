class Product:
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int):
        self.name: str = name
        self.description: str = description
        self._price: float = price
        self.quantity_in_stock: int = quantity_in_stock

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
        pt_summ = self.quantity_in_stock * self._price + other.quantity_in_stock * other.price
        return pt_summ





