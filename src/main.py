from mixing_class import MixingLog
from abc_class import SomeProduct


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
        list_goods = []
        for good in self.__goods:
            list_goods.append(str(good))
        return list_goods

    @goods.setter
    def add_good(self, good):
        """ Add product in list """
        if isinstance(good, Product):
            if good.quantity < 1:
                raise ValueError('Недопустимое для количества значение')
            self.__goods.append(good)
        else:
            raise TypeError

    def __str__(self):
        return f'{self.title}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        self.length = len(self.__goods)
        return self.length

    def middle_price(self, summ_of_prices=None):
        for product in self.__goods:
            summ_of_prices += product.get_price
        try:
            return summ_of_prices / len(self.__goods)
        except ZeroDivisionError:
            return 0


class Product(MixingLog, SomeProduct):
    title: str
    description: str
    __price: float
    quantity: int
    color: str

    def __init__(self, title, description, _price, quantity, color):
        self.title = title
        self.description = description
        self.__price = _price
        if quantity < 1:
            raise ValueError('Недопустимое для количества значение')
        self.quantity = quantity
        self.color = color
        super().__init__()

    @classmethod
    def create_product(cls, title, description, _price, quantity, color):
        """ Create and return new product """
        new_product = cls(title, description, _price, quantity, color)
        return new_product

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def set_price(self, price, interactive=True):
        """ Set new price """
        if self.__price > price and interactive:
            unswer = input('New price is higher than old price. Confirm price change: enter yes(y) or no(n).')
            if unswer.lower() in ['y', 'yes']:
                self.__price = price
        elif price > 0:
            self.__price = price
        else:
            print('Incorrect price')

    def __str__(self):
        return f'{self.title}, {self.__price}руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        summ_ = self.__price * self.quantity + other.__price * other.quantity
        return summ_