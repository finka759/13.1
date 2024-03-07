import json
import os

from src.category import Category
from src.lawn_grass import LawnGrass
from src.smartfon import Smartfon


def main():
    smartfon1 = Smartfon('smartfon_name1', 'smartfon_description1', 100, 10)
    smartfon2 = Smartfon('smartfon_name2', 'smartfon_description2', 200, 20)
    l_grass1 = LawnGrass('l_grass_name1', 'l_grass_description1', 300, 30)
    l_grass2 = LawnGrass('l_grass_name2', 'l_grass_description2', 400, 40)
    list_data = get_products_data()
    objects_list = make_objects_list_from_list(list_data)

    print(objects_list[0].get_average_price_of_all_products)
    print(objects_list[1].get_average_price_of_all_products)

    print('---')
    print('В классе «Категории» реализовать метод, который подсчитывает средний ценник всех товаров. С помощью '
          'исключений обработать случай, когда в категории нет товаров и сумма всех товаров будет делиться на ноль. В '
          'случае, если такое происходит, возвращать ноль.')
    print('---')
    middle_price_in_category_0 = objects_list[0].get_average_price_of_all_products
    print(f'middle_price_in_category_0 = {middle_price_in_category_0}')
    middle_price_in_category_1 = objects_list[1].get_average_price_of_all_products
    print(f'middle_price_in_category_1 = {middle_price_in_category_1}')

    print('---')
    print('Начало проверки 16.1_1 При добавлении товара с нулевым количеством вызывать исключение ValueError, '
          'которое будет сообщать пользователю, что товар с нулевым количеством не может быть добавлен. При этом '
          'прерывать выполнение программы.')
    print('---')
    summ_l_grasess_and_smartfon = l_grass1.__add__(smartfon1)
    print(f'summ_l_grasess_and_smartfon = {summ_l_grasess_and_smartfon} (не должно выполнится, и должно прерваться)')
    summ_l_grasess = l_grass1.__add__(l_grass2)
    print(f'summ_l_grasess = {summ_l_grasess} состоит из {l_grass1.quantity_in_stock} на {l_grass1.price} '
          f'и {l_grass2.quantity_in_stock} на {l_grass2.price}')


def get_products_data():
    """
    Функция получает строку json из файла
    :return: и возвращает список
    """
    way_to_json = os.path.join('..', 'sourses', 'products_data.json')
    with open(way_to_json, encoding='UTF-8') as products_data:
        data = json.load(products_data)
        return data


def make_objects_list_from_list(list_data):
    """
    Функция получает список
    :return: и возвращает список объектов Category c Products
    """
    list_ctgrs = []
    for category in list_data:
        list_obj_products = []
        for product in category['products']:
            list_obj_products.append(product)
        list_ctgrs.append(Category(category['name'], category['description'], list_obj_products))
    return list_ctgrs


if __name__ == "__main__":
    main()
