class Category:
    """
    Класс для категорий товара
    """

    number_of_categories: int = 0
    number_of_unique_products: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name: str = name
        self.description: str = description
        self.__products: list = products

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(products)

    # Геттер для products
    @property
    def products(self):
        list_product = []
        for products in self.__products:
            # list_product.append(f"{products['name']}, {products['price']} руб. Остаток: {products['quantity']} шт.\n")
            # list_product.append(products.__str__)
            list_product.append(str(products))
        return "".join(list_product)

    def add_to_products(self, product):
        self.__products.append(product)

    def __len__(self):
        pt_count: int = 0
        for product in self.__products:
            pt_count = pt_count + product.quantity_in_stock
        return pt_count

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."
