class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        pass