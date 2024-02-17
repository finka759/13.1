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
        self.__products: list = products

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(products)

    # Геттер для products
    @property
    def products(self):
        list_product = []
        for products in self.__products:
            list_product.append(f"{products['name']}, {products['price']} руб. Остаток: {products['quantity']} шт.\n")

        return "".join(list_product)

    # Сеттер для products

    def add_to_products(self, product):
        self.__products.append(product)


cat1 = Category('имя1', 'описание1', [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ])
cat1.add_to_products(Product())

print(cat1.products)
