import json
import os

from src.category import Category


def main():
    list_data = get_products_data()
    objects_list = make_objects_list_from_list(list_data)
    # print(objects_list[0].products)
    # print(objects_list[1].products)


def get_products_data():
    way_to_json = os.path.join('..', 'sourses', 'products_data.json')
    with open(way_to_json, encoding='UTF-8') as products_data:
        data = json.load(products_data)
        return data


def make_objects_list_from_list(list_data):
    list_ctgrs = []
    for category in list_data:
        list_obj_products = []
        for product in category['products']:
            list_obj_products.append(product)
        list_ctgrs.append(Category(category['name'], category['description'], list_obj_products))
    return list_ctgrs


if __name__ == "__main__":
    main()
