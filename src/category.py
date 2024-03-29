from src.mixin_log import MixinLog
from src.product import Product
from src.zero_add_exception import ZeroAddException


class Category(MixinLog):
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
        super().__init__()

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
            raise TypeError("Добавлять можно только объекты Product или его наследников!")
        elif product.quantity_in_stock == 0:
            try:
                raise ZeroAddException('Попытка добавления товара со значением quantity_in_stock ноль!')
            except ZeroAddException as e:
                print(e)
        else:
            if self.__products.append(product):
                print('Товар добавлен в категорию!')
        print('Oбработка добавления товара завершена.')

    def __len__(self):
        pt_count: int = 0
        for product in self.__products:
            pt_count = pt_count + product.quantity_in_stock
        return pt_count

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    # геттер для класса CategoryIterProd  и для get_average_price_of_all_products
    @property
    def products_list(self):
        return self.__products

    @property
    def get_average_price_of_all_products(self):
        len_ = 0
        summ = 0
        try:
            if not self.products_list:
                er_message = f'В категории {self.name} нет продуктов! Категория {self.name} пустая!'
                raise ValueError(er_message)
        except ValueError as e:
            print(e)
            return 0

        for product in self.products_list:
            len_ += product.quantity_in_stock
            summ += summ + product.price

        try:
            if len_ == 0:
                er_message = (f'Нельзя посчитать среднее значение цены продуктов в категории {self.name}!'
                              f'Всего продуктов в категории {self.name} - 0!')
                raise ZeroDivisionError(er_message)
        except ZeroDivisionError as e:
            print(e)
            return 0

        result = round(summ / len_, 2)
        return result
