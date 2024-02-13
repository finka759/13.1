class Category:
    """ Для класса Category определите следующие свойства:
        название,
        описание,
        товары.
        А также для класса Category добавьте два атрибута, в которых будут храниться
        - общее количество категорий и
        - общее количество уникальных продуктов,
         не учитывая количество в наличии."""

    ctgry_name: str
    ctgry_description: str
    ctgry_products: list

    ctgry_number_of_categories = 0
    ctgry_number_of_unique_products = 0

    def __init__(self, ctgry_name, ctgry_description, ctgry_products):
        self.ctgry_name = ctgry_name
        self.ctgry_description = ctgry_description
        self.ctgry_products = ctgry_products

        Category.ctgry_number_of_categories += 1
        Category.ctgry_number_of_unique_products += len(ctgry_products)

