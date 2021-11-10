from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    def __init__(self, username: str, health: int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.__health = value

    @property
    def is_dead(self):
        return self.health <= 0

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points

#
#
# from unittest import TestCase, main
#
#
# class TestPlayer(TestCase):
#     def setUp(self) -> None:
#         self.player = Player('a', 10)
#
#     def test_player_name_with_empty_str_raise_error(self):
#         with self.assertRaises(ValueError) as exc:
#             self.player.username = ''
#         self.assertEqual(str(exc.exception), "Player's username cannot be an empty string.")
#
#     def test_player_name_successfully(self):
#         self.assertEqual(self.player.username, 'a')
#
#     def test_health_with_positive_value(self):
#         self.assertEqual(self.player.health, 10)
#
#     def test_health_is_zero_or_minus_value_raise_error(self):
#         with self.assertRaises(ValueError) as exc:
#             self.player.health = -1
#         self.assertEqual(str(exc.exception), "Player's health bonus cannot be less than zero.")
#
#     def test_is_dead_with_zero(self):
#         self.player.health = 0
#         self.assertTrue(self.player.is_dead)
#
#     def test_is_dead_with_positive_value(self):
#         self.player.health = 1
#         self.assertEqual(self.player.health, 1)
#
#
# if __name__ == '__main__':
#     main()
