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
    def get_goods(self):
        """ Return title, price and quantity of every product"""
        for good in self.__goods:
            return f'{good.title}, {good.price} руб. Остаток: {good.quantity} шт.'

    @get_goods.setter
    def add_good(self, good):
        """ Add product in list """
        self.__goods.append(good)


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
        elif price > 0:
            self.__price = price
        else:
            print('Incorrect price')
