from unittest import TestCase, main

from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room('a', 1000, 2)

    def test_init(self):
        self.assertEqual(self.room.family_name, 'a')
        self.assertEqual(self.room.budget, 1000)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_expenses_with_minus_value_raises_error(self):
        with self.assertRaises(ValueError) as exc:
            self.room.expenses = -1
        self.assertEqual(str(exc.exception),"Expenses cannot be negative")

    def test_expenses_successfully_added(self):
        self.room.expenses = 1
        self.assertEqual(self.room.expenses, 1)

    def test_calculate_expenses_for_child(self):
        ch1 = Child(5, 1, 2, 1)
        ch2 = Child(5, 1)
        self.room.calculate_expenses([ch1, ch2])
        self.assertEqual(self.room.expenses, 450)

    def test_calculate_expenses_for_appliances(self):
        appliances = [TV(), Fridge(), Laptop()] * 2
        self.room.calculate_expenses(appliances)
        self.assertEqual(self.room.expenses, 222)

if __name__ == '__main__':
    main()
