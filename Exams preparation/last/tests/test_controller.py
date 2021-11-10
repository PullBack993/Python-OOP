from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_init(self):
        self.assertIsInstance(self.controller.player_repository, PlayerRepository)
        self.assertIsInstance(self.controller.card_repository, CardRepository)

    def test_add_player(self):
        self.controller.add_player('Beginner', 'a')

        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertIsInstance(self.controller.player_repository.players[0], Beginner)

    def test_message_from_add_player(self):
        msg = f"Successfully added player of type Beginner with username: a"
        result = self.controller.add_player('Beginner', 'a')
        self.assertEqual(result, msg)

    def test_add_card(self):
        self.controller.add_card('Magic', 'a')
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertIsInstance(self.controller.card_repository.cards[0], MagicCard)

    def test_message_from_add_card(self):
        msg = "Successfully added card of type MagicCard with name: a"
        result = self.controller.add_card('Magic', 'a')
        self.assertEqual(result, msg)

    def test_add_player_card(self):
        self.controller.add_player('Beginner', 'a')
        self.controller.add_card('Magic', 'm')
        self.controller.add_player_card('a', 'm')
        res = self.controller.player_repository.players[0].card_repository.cards[0].name
        self.assertEqual('m', res)

    def test_add_player_card_message(self):
        self.controller.add_player('Beginner', 'a')
        self.controller.add_card('Magic', 'm')
        msg = "Successfully added card: m to user: a"
        result = self.controller.add_player_card('a', 'm')
        self.assertEqual(result, msg)

    def test_fight(self):
        self.controller.add_player('Beginner', 'a')
        self.controller.add_player('Advanced', 'ad')
        self.controller.add_card('Magic', 'm')
        self.controller.add_player_card('a', 'm')
        expected = f"Attack user health 170 - Enemy user health 215"
        result = self.controller.fight('a', 'ad')
        self.assertEqual(expected, result)

    # def test_fight_take_damage(self):
    #     self.controller.add_player('Beginner', 'a')
    #     a = Player('a', -1)
    #     self.controller.add_card('Magic', 'm')
    #     self.controller.add_player_card('a', 'm')
    #     with self.assertRaises(ValueError) as exc:
    #         self.controller.fight('a', 'ad')
    #         a = [card.damage_points for card in self.controller.card_repository.cards]
    #         a = -1
    #     self.assertEqual(str(exc.exception), "Damage points cannot be less than zero.")

    def test_report(self):
        self.controller.add_player('Beginner', 'a')
        self.controller.add_player('Beginner', 'b')
        self.controller.add_card('Trap', 'at')
        self.controller.add_card('Trap', 'bt')
        self.controller.add_player_card('a', 'at')
        self.controller.add_player_card('b', 'bt')
        res = self.controller.report()
        exp = "Username: a - Health: 50 - Cards 1\n" \
              "### Card: at - Damage: 120\n" \
              "Username: b - Health: 50 - Cards 1\n" \
              "### Card: bt - Damage: 120\n"
        self.assertEqual(exp, res)


if __name__ == '__main__':
    main()
