import json
import os

from src.category import Category
from src.lawn_grass import LawnGrass
from src.smartfon import Smartfon


def main():
    smartfon1 = Smartfon('smartfon_name1', 'smartfon_description1', 100, 10)
    smartfon2 = Sm1 = Smartfon('smartfon_name2', 'smartfon_description2', 200, 20)
    l_grass1 = LawnGrass('l_grass_name1', 'l_grass_description1', 300, 30)
    l_grass2 = LawnGrass('l_grass_name2', 'l_grass_description2', 400, 40)
    list_data = get_products_data()
    objects_list = make_objects_list_from_list(list_data)

    print(objects_list[0].get_average_price_of_all_products)
    print(objects_list[1].get_average_price_of_all_products)


def get_products_data():
    '''
    Функция получает строку json из файла
    :return: и возвращает список
    '''
    way_to_json = os.path.join('..', 'sourses', 'products_data.json')
    with open(way_to_json, encoding='UTF-8') as products_data:
        data = json.load(products_data)
        return data


def make_objects_list_from_list(list_data):
    '''
    Функция получает список
    :return: и возвращает список объектов Category c Products
    '''
    list_ctgrs = []
    for category in list_data:
        list_obj_products = []
        for product in category['products']:
            list_obj_products.append(product)
        list_ctgrs.append(Category(category['name'], category['description'], list_obj_products))
    return list_ctgrs


if __name__ == "__main__":
    main()
