class Category:

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)
