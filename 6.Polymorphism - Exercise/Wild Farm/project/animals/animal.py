from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    def feed(self, food: Food):
        if self._FOOD_PREFERENCES and not isinstance(food, self._FOOD_PREFERENCES):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * self._WEIGHT_GAIN_PER_FOOD
        self.food_eaten += food.quantity

    @property
    @abstractmethod
    def _FOOD_PREFERENCES(self):
        pass

    @property
    @abstractmethod
    def _WEIGHT_GAIN_PER_FOOD(self):
        pass

    @abstractmethod
    def make_sound(self):
        ...


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return '{type} [{name}, {wing_size}, {weight}, {food_eaten}]'.format(
            type=self.__class__.__name__,
            name=self.name,
            wing_size=self.wing_size,
            weight=self.weight,
            food_eaten=self.food_eaten
        )


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return '{type} [{name}, {weight}, {living_region}, {food_eaten}]'.format(
            type=self.__class__.__name__,
            name=self.name,
            weight=self.weight,
            living_region=self.living_region,
            food_eaten=self.food_eaten

        )
