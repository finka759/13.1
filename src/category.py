class Category:
    """
    Класс для категорий товара
    """

    number_of_categories: int = 0
    number_of_unique_products: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.products: list = products

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(products)
