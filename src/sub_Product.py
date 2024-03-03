from main import Product


class Smartphone(Product):
    title: str
    description: str
    __price: float
    quantity: int
    color: str
    performance: str
    model: str
    memory: float

    def __init__(self, title, description, _price, quantity, performance, model, memory, color):
        super().__init__(title, description, _price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory

    @classmethod
    def create_product(cls, title, description, _price, quantity, performance, model, memory, color):
        """ Create and return new product """
        new_product = cls(title, description, _price, quantity, performance, model, memory, color)
        return new_product

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return super().__add__(self)

        raise TypeError


class LawnGrass(Product):
    title: str
    description: str
    __price: float
    quantity: int
    color: str
    country: str
    growing_time: float

    def __init__(self, title, description, _price, quantity, country, growing_time, color):
        super().__init__(title, description, _price, quantity, color)
        self.country = country
        self.growing_time = growing_time

    @classmethod
    def create_product(cls, title, description, _price, quantity, country, growing_time, color):
        """ Create and return new product """
        new_product = cls(title, description, _price, quantity, country, growing_time, color)
        return new_product

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return super().__add__(self)

        raise TypeError