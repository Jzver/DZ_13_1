import unittest


class TestCategoryAndProduct(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", "Electronics products")
        self.product1 = Product("Phone", "Smartphone", 1000, 10)
        self.product2 = Product("TV", "Television", 2000, 5)

    def test_category_initialization(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Electronics products")
        self.assertEqual(self.category.products, [])
        self.assertEqual(Category.total_categories, 1)

    def test_product_initialization(self):
        self.assertEqual(self.product1.name, "Phone")
        self.assertEqual(self.product1.description, "Smartphone")
        self.assertEqual(self.product1.price, 1000)
        self.assertEqual(self.product1.quantity, 10)
        self.assertEqual(Category.total_unique_products, 2)

    def test_count_products(self):
        self.assertEqual(len(self.category.products), 0)
        self.category.products.append(self.product1)
        self.assertEqual(len(self.category.products), 1)
        self.category.products.append(self.product2)
        self.assertEqual(len(self.category.products), 2)


if __name__ == "__main__":
    unittest.main()
