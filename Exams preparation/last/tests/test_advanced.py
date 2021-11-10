from unittest import TestCase, main

from project.player.advanced import Advanced
from project.player.player import Player


class TestAdvanced(TestCase):
    def setUp(self):
        self.advanced = Advanced('A')

    def test_init_attr(self):
        self.assertEqual(self.advanced.username, 'A')
        self.assertEqual(self.advanced.health, 250)

    def test_inherits_from_player(self):
        self.assertIsInstance(self.advanced, Advanced)
        self.assertIsInstance(self.advanced, Player)
        self.assertTrue(issubclass(Advanced, Player))

    def test_username__when_empty__should_raise(self):
        with self.assertRaises(ValueError) as exc:
            Advanced('')
        msg = "Player's username cannot be an empty string."
        self.assertEqual(msg, str(exc.exception))

    def test_health__when_negative__should_raise(self):
        with self.assertRaises(ValueError) as exc:
            self.advanced.health = -1
        msg = "Player's health bonus cannot be less than zero."
        self.assertEqual(msg, str(exc.exception))

    def test_player_take_damage_raise_error(self):
        with self.assertRaises(ValueError) as exc:
            self.advanced.take_damage(-1)
        self.assertEqual(str(exc.exception), "Damage points cannot be less than zero.")

if __name__ == '__main__':
    main()


