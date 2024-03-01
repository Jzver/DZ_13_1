import pytest
from src.main import Category, Product


@pytest.fixture
def some_product():
    return Product('Soap', 'soap for hands', 50, 15, 'color')


@pytest.fixture
def some_product_1():
    return Product('Spoon', 'spoon for soup', 120, 6, 'color')


def test_init(some_product):
    assert some_product.title == 'Soap'
    assert some_product.description == 'soap for hands'
    assert some_product.get_price() == 50
    assert some_product.quantity == 15
    assert some_product.color == 'color'


def test_create_product():
    assert isinstance(Product.create_product('Soap'), Product)


def test_str(some_product):
    assert str(some_product) == 'Soap, 50руб. Остаток: 15 шт.'


def test_add(some_product, some_product_1):
    assert some_product + some_product_1 == 1470
