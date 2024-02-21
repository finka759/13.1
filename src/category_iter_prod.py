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
