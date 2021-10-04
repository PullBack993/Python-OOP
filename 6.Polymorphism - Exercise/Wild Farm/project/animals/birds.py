from project.food import Food, Meat
from project.animals.animal import Bird


class Owl(Bird):
    _FOOD_PREFERENCES = (Meat,)
    _WEIGHT_GAIN_PER_FOOD = 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    _FOOD_PREFERENCES = None
    _WEIGHT_GAIN_PER_FOOD = 0.35

    def make_sound(self):
        return 'Cluck'
