import pytest

from src.product import Product


@pytest.fixture
def class_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


def test_product_init(class_product):
    assert class_product.prdct_name == 'Samsung Galaxy C23 Ultra'
    assert class_product.prdct_description == '256GB, Серый цвет, 200MP камера'
    assert class_product.prdct_price == 180000.0
    assert class_product.prdct_quantity_in_stock == 5

