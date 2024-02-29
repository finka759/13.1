from src.mixin_log import MixinLog
from src.product import Product


class LawnGrass(Product, MixinLog):

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int, colour: str = None,
                 country_of_manufacture: str = None, germination_period: str = None):
        super().__init__(name, description, price, quantity_in_stock, colour)
        self.country_of_manufacture = country_of_manufacture
        self.germination_period = germination_period
