import pytest

from mixing_class import MixingLog
from abc_class import SomeProduct
from main import Category, Product


# Test class for Category
@pytest.fixture
def category_fixture():
    goods = Product('product1', 'desc', 100, 5, 'blue'), Product('product2', 'desc', 200, 10, 'red')
    cat = Category('Cat1', 'desc', goods)
    return cat


def test_category_init(category_fixture):
    assert isinstance(category_fixture, Category)
    assert category_fixture.title == 'Cat1'
    assert category_fixture.description == 'desc'
    assert len(category_fixture.goods) == 2


def test_category_add_good(category_fixture):
    with pytest.raises(ValueError):
        category_fixture.add_good(Product('product3', 'desc', 300, 0, 'green'))
    category_fixture.add_good(Product('product3', 'desc', 300, 5, 'green'))
    assert len(category_fixture.goods) == 3


def test_category_middle_price(category_fixture):
    assert pytest.approx(category_fixture.middle_price(), 0.01) == 150.0


# Test class for Product
@pytest.fixture
def product_fixture():
    product = Product('prod1', 'desc', 200, 2, 'blue')
    return product


def test_product_init(product_fixture):
    assert isinstance(product_fixture, Product)
    assert product_fixture.title == 'prod1'
    assert product_fixture.description == 'desc'
    assert product_fixture.price == 200
    assert product_fixture.quantity == 2
    assert product_fixture.color == 'blue'


def test_product_set_price(product_fixture):
    product_fixture.set_price(-1)
    assert product_fixture.price == 200
    product_fixture.set_price(300, interactive=False)
    assert product_fixture.price == 300


def test_product_add():
    product1 = Product('prod1', 'desc', 200, 2, 'blue')
    product2 = Product('prod2', 'desc', 300, 3, 'green')
    assert product1 + product2 == (200 * 2 + 300 * 3)
