from src.product import Product


class LawnGrass(Product):

    def __init__(self, country_of_manufacture: str, germination_period: str, colour: str, name: str, description: str,
                 price: float, quantity_in_stock: int):
        super().__init__(name, description, price, quantity_in_stock, colour)
        self.country_of_manufacture = country_of_manufacture
        self.germination_period = germination_period

