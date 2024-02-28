from src.product import Product


class Category:
    """
    Класс для категорий товара
    """

    number_of_categories: int = 0
    number_of_unique_products: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.__products: list = []
        for product in products:
            self.__products.append(
                Product(product['name'], product['description'], product['price'], product['quantity']))

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(products)

    # Геттер для products
    @property
    def products(self):
        list_product = []
        for product in self.__products:
            list_product.append(str(product))
        return "\n".join(list_product)

    def add_to_products(self, product):
        if not isinstance(product, self.__class__):
            raise TypeError("Добавлять можно только объекты Product или его наследников")
        else:
            self.__products.append(product)

    def __len__(self):
        pt_count: int = 0
        for product in self.__products:
            pt_count = pt_count + product.quantity_in_stock
        return pt_count

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    # геттер для класса CategoryIterProd
    @property
    def products_list(self):
        return self.__products
