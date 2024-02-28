import pytest

from src.product import Product


@pytest.fixture
def class_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


def test_product_init(class_product):
    assert class_product.name == 'Samsung Galaxy C23 Ultra'
    assert class_product.description == '256GB, Серый цвет, 200MP камера'
    assert class_product.price == 180000.0
    assert class_product.quantity_in_stock == 5
    assert class_product.colour is None


def test___str__(class_product):
    assert str(class_product) == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test___add__(class_product):
    assert class_product + class_product == 180000.0 * 5 * 2
