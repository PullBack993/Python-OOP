from animals.animal import Animal


class Lion(Animal):
    def __init__(self, name, gender, age, money_for_care=50):
        self.money_for_care = money_for_care
        super().__init__(name, gender, age)

    @staticmethod
    def get_needs():
        return 50
