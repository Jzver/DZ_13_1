class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def get_product(self):
        return self.__products


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.total_unique_products += 1


if __name__ == "__main__":
    category1 = Category("Electronics", "Electronics products")
    product1 = Product("Phone", "Smartphone", 1000, 10)

    products = ["Товар 1", "Товар 2", "Товар 3"]
    category = Category("Категория", "Описание", products)

print(category.get_products())  # Выводит: ["Товар 1", "Товар 2", "Товар 3"]