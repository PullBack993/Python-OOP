from project.people.child import Child

class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        res = 0
        for el in args:
            for x in el:
                if x.__class__.__name__ == 'Child':
                    res += x.cost * 30
                else:
                    res += x.get_monthly_expense()
        self.expenses = res
