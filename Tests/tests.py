import pytest


@pytest.fixture
def category():
    return Category("Electronics", "Electronics products")


@pytest.fixture
def product1():
    return Product("Phone", "Smartphone", 1000, 10)


@pytest.fixture
def product2():
    return Product("TV", "Television", 2000, 5)


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Electronics products"
    assert category.products == []
    assert Category.total_categories == 1


def test_product_initialization(product1):
    assert product1.name == "Phone"
    assert product1.description == "Smartphone"
    assert product1.price == 1000
    assert product1.quantity == 10


def test_count_products(category, product1, product2):
    category.add_product(product1)
    category.add_product(product2)
    assert category.count_products() == 2


def test_count_categories(category):
    assert Category.total_categories == 1
