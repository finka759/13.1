class Product:
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int):
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity_in_stock: int = quantity_in_stock
