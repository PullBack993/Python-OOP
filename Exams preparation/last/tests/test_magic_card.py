from unittest import TestCase, main

from project.card.card import Card
from project.card.magic_card import MagicCard


class TestAdvanced(TestCase):
    def setUp(self):
        self.magic_card = MagicCard('A')

    def test_init_attr(self):
        self.assertEqual(self.magic_card.name, 'A')
        self.assertEqual(self.magic_card.damage_points, 5)
        self.assertEqual(self.magic_card.health_points, 80)

    def test_inherits_from_card(self):
        self.assertIsInstance(self.magic_card, MagicCard)
        self.assertIsInstance(self.magic_card, Card)
        self.assertTrue(issubclass(MagicCard, Card))

    def test_name_empty_raises_error(self):
        with self.assertRaises(ValueError) as exc:
            self.magic_card.name = ""
        self.assertEqual(str(exc.exception), "Card's name cannot be an empty string.")

    def test_health_points_minus_value_raises_error(self):
        with self.assertRaises(ValueError) as exc:
            self.magic_card.health_points = -1
        self.assertEqual(str(exc.exception), "Card's HP cannot be less than zero.")

    def test_damage_points_cannot_be_below_zero(self):
        with self.assertRaises(ValueError) as exc:
            self.magic_card.damage_points = -1
        self.assertEqual(str(exc.exception),"Card's damage points cannot be less than zero.")

if __name__ == '__main__':
    main()
