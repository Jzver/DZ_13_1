class Category:
    title: str
    description: str
    goods: list

    count = 0
    unique = 0

    def __init__(self, title, description, goods):
        self.title = title
        self.description = description
        self.__goods = goods

        Category.count += 1
        Category.unique += len(set(self.__goods))

    @property
    def goods(self):
        """ Return title, price and quantity of every product"""
        for good in self.__goods:
            return str(Product)

    @goods.setter
    def add_good(self, good):
        """ Add product in list """
        self.__goods.append(good)

    def __str__(self):
        return f'{self.title}, quantity of products: {len(self)} pcs.'

    def __len__(self):
        self.length = len(self.__goods)
        return self.length


class Product:
    title: str
    description: str
    price: float
    quantity: int

    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, title, description, price, quantity):
        """ Create and return new product """
        new_product = cls(title, description, price, quantity)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def new_price(self, price):
        """ Set new price """
        if self.__price > price:
            unswer = input('New price is higher than old price. Confirm price change: enter yes(y) or no(n).')
            if unswer == 'y' or unswer == 'yes':
                self.__price = price

    def __str__(self):
        return f'{self.title}, {self.__price}. Remaining amount: {self.quantity} pcs.'

    def __add__(self, other):
        summ_ = self.__price * self.quantity + other.__price * other.quantity
        return summ_
