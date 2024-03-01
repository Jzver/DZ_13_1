from main import Product


class Smartphone(Product):
    def __init__(self, title, description, _price, quantity, performance, model, memory):
        super().__init__(title, description, _price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory

    @classmethod
    def create_product(cls):
        """ Create and return new product """
        new_product = cls(title, description, _price, quantity, performance, model, memory, color)
        return new_product

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return super().__add__(self, other)

        raise TypeError


class LawnGrass(Product):
    def __init__(self, title, description, _price, quantity, country, growing_time, color):
        super().__init__(title, description, _price, quantity, color)
        self.country = country
        self.growing_time = growing_time

    @classmethod
    def create_product(cls):
        """ Create and return new product """
        new_product = cls(title, description, _price, quantity, country, growing_time, color)
        return new_product

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return super().__add__(self)

        raise TypeError


lawn_grass = LawnGrass('title', 'description', '_price', 'quantity', 'country', 'growing_time', 'color')
phone = Smartphone('title', 'description', '_price', 'quantity', 'performance', 'model', 'memory', 'color')

print(lawn_grass)
print(phone)
