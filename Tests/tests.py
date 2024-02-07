from main import Category, Product  # Replace "your_module" with the actual module name


def test_category_initialization():
    category = Category("Electronics", "Electronics products")
    assert category.name == "Electronics"
    assert category.description == "Electronics products"
    assert category.products == []
    assert Category.total_categories == 2


def test_product_initialization():
    product1 = Product("Phone", "Smartphone", 1000, 10)
    assert product1.name == "Phone"
    assert product1.description == "Smartphone"
    assert product1.price == 1000
    assert product1.quantity == 10


def test_count_categories():
    assert Category.total_categories == 2

def test_count_total_unique_products():
    assert Category.total_unique_products == 2
