import json

from src.category import Category
from src.product import Product


def main():
    list_data = get_products_data()
    print(list_data)
    objects_list = make_objects_list_from_list(list_data)
    print(objects_list[0].products[0].name)


def get_products_data():
    with open('../sourses/products_data.json', encoding='UTF-8') as products_data:
        data = json.load(products_data)
        return data


def make_objects_list_from_list(list_data):
    list_ctgrs = []
    for category in list_data:
        list_obj_products = []
        for product in category['products']:
            list_obj_products.append(
                Product(product['name'], product['description'], product['price'], product['quantity']))
        list_ctgrs.append(Category(category['name'], category['description'], list_obj_products))
    return list_ctgrs


if __name__ == "__main__":
    main()
