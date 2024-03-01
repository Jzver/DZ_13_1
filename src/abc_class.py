from abc import ABC, abstractmethod


class SomeProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def __add__(self):
        pass