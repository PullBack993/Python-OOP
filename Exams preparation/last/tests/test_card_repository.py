from unittest import TestCase, main

from project.card.card import Card
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(TestCase):
    def setUp(self):
        self.card_rep = CardRepository()
        self.magic_card = MagicCard('A')

    def test_init(self):
        self.assertEqual(0, self.card_rep.count)
        self.assertListEqual([], self.card_rep.cards)

    def test_add_to_card_with_same_name_raise_error(self):
        self.card_rep.add(self.magic_card)
        new_card = MagicCard('A')
        with self.assertRaises(ValueError) as exc:
            self.card_rep.add(new_card)
        self.assertEqual(str(exc.exception), "Card A already exists!")

    def test_add_card_successfully(self):
        self.card_rep.add(self.magic_card)
        self.assertIn(self.magic_card, self.card_rep.cards)

    def test_after_add_a_card_count_increase(self):
        self.card_rep.add(self.magic_card)
        self.assertEqual(self.card_rep.count, 1)

    def test_after_remove_should_be_decrease_count(self):
        self.card_rep.add(self.magic_card)
        self.assertEqual(self.card_rep.count, 1)
        self.card_rep.remove('A')
        self.assertEqual(self.card_rep.count, 0)

    def test_remove_card_raise_error(self):
        with self.assertRaises(ValueError) as exc:
            self.card_rep.remove("")
        self.assertEqual(str(exc.exception), "Card cannot be an empty string!")

    def test_remove_card_successfully(self):
        self.card_rep.add(self.magic_card)
        self.assertEqual(self.card_rep.count, 1)
        self.card_rep.remove('A')
        self.assertNotIn(self.magic_card, self.card_rep.cards)
        self.assertEqual(self.card_rep.cards, [])

    def test_find_card(self):
        self.card_rep.add(self.magic_card)
        result = self.card_rep.find('A')
        self.assertEqual(self.magic_card, result)

if __name__ == '__main__':
    main()
