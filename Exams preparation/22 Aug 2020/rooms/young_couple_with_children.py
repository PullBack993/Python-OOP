from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name=family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)


# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
# print(young_couple_with_children.expenses)
# for ap in young_couple_with_children.appliances:
#     print(ap)
#     print(ap.cost)
#     print(ap.get_monthly_expense())
#     print()