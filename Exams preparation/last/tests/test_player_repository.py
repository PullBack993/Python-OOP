from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestCardRepository(TestCase):
    def setUp(self):
        self.player_rep = PlayerRepository()
        self.beginner = Beginner('A')

    def test_init(self):
        self.assertEqual(0, self.player_rep.count)
        self.assertListEqual([], self.player_rep.players)

    def test_add_to_player_with_same_name_raise_error(self):
        self.player_rep.add(self.beginner)
        new_card = Beginner('A')
        with self.assertRaises(ValueError) as exc:
            self.player_rep.add(new_card)
        self.assertEqual(str(exc.exception), f"Player A already exists!")

    def test_add_player_successfully(self):
        self.player_rep.add(self.beginner)
        self.assertIn(self.beginner, self.player_rep.players)
        self.assertEqual(self.player_rep.count, 1)

    def test_after_add_a_player_count_increase(self):
        self.player_rep.add(self.beginner)
        self.assertEqual(self.player_rep.count, 1)

    def test_after_remove_should_be_decrease_count(self):
        self.player_rep.add(self.beginner)
        self.assertEqual(self.player_rep.count, 1)
        self.player_rep.remove('A')
        self.assertEqual(self.player_rep.count, 0)

    def test_remove_player_raise_error(self):
        with self.assertRaises(ValueError) as exc:
            self.player_rep.remove("")
        self.assertEqual(str(exc.exception), "Player cannot be an empty string!")

    def test_remove_player_successfully(self):
        self.player_rep.add(self.beginner)
        self.assertEqual(self.player_rep.count, 1)
        self.player_rep.remove('A')
        self.assertEqual(self.player_rep.count, 0)
        self.assertNotIn(self.beginner, self.player_rep.players)
        self.assertEqual(self.player_rep.players, [])

    def test_find_player(self):
        self.player_rep.add(self.beginner)
        result = self.player_rep.find('A')
        self.assertEqual(self.beginner, result)

if __name__ == '__main__':
    main()
