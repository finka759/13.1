import pytest

from src.category import Category


@pytest.fixture
def class_category():
    return Category('Смартфоны',
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


def test_init(class_category):
    assert class_category.ctgry_name == 'Смартфоны'
    assert class_category.ctgry_description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_category.ctgry_products == [{
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }, {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    }]
    assert class_category.ctgry_number_of_categories == 1
    assert class_category.ctgry_number_of_unique_products == 2
