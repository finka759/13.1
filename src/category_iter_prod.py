from src.category import Category


class CategoryIterProd:

    def __init__(self, category: Category):
        self.category = category
        self.len: int = len(category)

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        pass
