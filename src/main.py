from src.category import Category


def main():
    category_1 = Category('name_1', 'description_1', [1, 2, 3, 4, 5])
    print(category_1.ctgry_name)
    print(category_1.ctgry_number_of_categories)


if __name__ == "__main__":
    main()
