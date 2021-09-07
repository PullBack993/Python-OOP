from animals.animal import Animal


class Cheetah(Animal):
    def __init__(self, name, gender, age, money_for_care=60):
        super().__init__(name, gender, age)
        self.money_for_care = money_for_care

    @staticmethod
    def get_needs():
        return 60
