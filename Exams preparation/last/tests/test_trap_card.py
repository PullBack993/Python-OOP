from unittest import TestCase, main

from project.card.card import Card
from project.card.trap_card import TrapCard


class TestAdvanced(TestCase):
    def setUp(self):
        self.trap_card = TrapCard('A')

    def test_init_attr(self):
        self.assertEqual(self.trap_card.name, 'A')
        self.assertEqual(self.trap_card.damage_points, 120)
        self.assertEqual(self.trap_card.health_points, 5)

    def test_inherits_from_card(self):
        self.assertIsInstance(self.trap_card, TrapCard)
        self.assertIsInstance(self.trap_card, Card)
        self.assertTrue(issubclass(TrapCard, Card))

if __name__ == '__main__':
    main()
