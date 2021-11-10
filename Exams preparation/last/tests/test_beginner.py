from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player import Player


class TestBeginner(TestCase):
    def setUp(self):
        self.beginner = Beginner('A')

    def test_init_attr(self):
        self.assertEqual(self.beginner.username, 'A')
        self.assertEqual(self.beginner.health, 50)

    def test_inherits_from_player(self):
        self.assertIsInstance(self.beginner, Player)
        self.assertTrue(issubclass(Beginner, Player))


if __name__ == '__main__':
    main()
