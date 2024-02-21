import pytest

from src.category import Category


@pytest.fixture
def class_category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для '
                    'удобства жизни',
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


def test_init(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == ('Смартфоны, как средство не только коммуникации, но и получение '
                                          'дополнительных функций для удобства жизни')

    assert class_category.number_of_categories == 1
    assert class_category.number_of_unique_products == 2


def test_products(class_category):
    assert str(class_category.products) == (
        'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.')


def test___str__(class_category):
    assert str(class_category) == 'Смартфоны, количество продуктов: 13 шт.'
