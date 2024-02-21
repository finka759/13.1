from src.category import Category


class CategoryIterProd:

    def __init__(self, category: Category):
        self.name = category.name
        self.products_list = category.products_list
        self.lenght: int = len(category.products_list)

    def __iter__(self):
        self.current_val = -1
        return self

    def __next__(self):
        if self.current_val + 1 < self.lenght:
            self.current_val += 1
            return self.products_list[self.current_val]
        else:
            raise StopIteration


cat2 = Category('Смартфоны',
                'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                [{
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                }, {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                }])

cat_it = CategoryIterProd(cat2)

# print(cat_it.products_list)
print(cat_it.lenght)
for cat_item in cat_it:
    print(cat_item)
