from project_1.medicine.medicine import Medicine


class Painkiller(Medicine):
    def __init__(self):
        super().__init__(health_increase=20)
