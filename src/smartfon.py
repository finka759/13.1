from src.product import Product


class Smartfon(Product):

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int, colour: str = None,
                 efficiency: str = None, model: str = None, amount_of_internal_memory: str = None):
        super().__init__(name, description, price, quantity_in_stock, colour)
        self.efficiency = efficiency
        self.model = model
        self.amount_of_internal_memory = amount_of_internal_memory
