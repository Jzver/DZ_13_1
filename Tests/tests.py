import pytest
from src.main import Category, Product


@pytest.fixture
def some_category():
    return Category('home_apl', 'some goods for home', ['soap', 'spoon', 'knife', 'spoon', 'brush'])


def test_init(some_category):
    assert some_category.title == 'home_apl'
    assert some_category.description == 'some goods for home'


@pytest.fixture
def some_product():
    return Product('soap', 'soap for hands', 250, 15)


def test_init_product(some_product):
    assert some_product.title == 'soap'
    assert some_product.description == 'soap for hands'
    assert some_product.price == 250
    assert some_product.quantity == 15


def test_str(some_category):
    assert str(some_category) == 'home_apl, quantity of products: 5 pcs.'


def test_len(some_category):
    assert len(some_category) == 5
