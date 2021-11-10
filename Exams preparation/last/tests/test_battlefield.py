from unittest import TestCase, main

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player import Player


class TestBattleField(TestCase):
    def setUp(self):
        self.bf = BattleField()
        self.player = Player('A', 10)
        self.attacker = Beginner('a')
        self.enemy = Advanced('aa')

    def test_fight_attacker_is_dead(self):
        attacker = Advanced('A')
        enemy = Beginner('B')
        with self.assertRaises(ValueError) as exc:
            enemy.take_damage(50)
            self.bf.fight(attacker, enemy)
        self.assertEqual(str(exc.exception), "Player is dead!")

    def test_attacker_is_beginner_take_bonus_health(self):
        self.bf.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 90)

    def test_enemy_is_beginner_take_bonus_health(self):
        attacker = Advanced('a')
        enemy = Beginner('b')
        self.bf.fight(attacker, enemy)
        self.assertEqual(enemy.health, 90)

    def test_attacker_take_bonus_damage_points(self):
        card_one = MagicCard('b')
        card_two = TrapCard('c')
        self.attacker.card_repository.cards.append(card_one)
        self.attacker.card_repository.cards.append(card_two)
        self.bf.fight(self.attacker, self.enemy)
        self.assertEqual(185, sum([c.damage_points for c in self.attacker.card_repository.cards]))

    def test_enemy_take_bonus_damage_points(self):
        attacker = Advanced('a')
        enemy = Beginner('aa')
        card_one = MagicCard('b')
        card_two = TrapCard('c')
        enemy.card_repository.cards.append(card_one)
        enemy.card_repository.cards.append(card_two)
        self.bf.fight(attacker, enemy)
        self.assertEqual(185, sum([c.damage_points for c in enemy.card_repository.cards]))

    def test_attacker_take_health_from_cards(self):
        card_one = MagicCard('b')
        card_two = TrapCard('c')
        self.attacker.card_repository.cards.append(card_one)
        self.attacker.card_repository.cards.append(card_two)
        self.bf.get_bonus(self.attacker)
        self.assertEqual(self.attacker.health, 135)

    def test_enemy_take_health_from_cards(self):
        card_one = MagicCard('b')
        card_two = TrapCard('c')
        enemy = Beginner('abc')
        enemy.card_repository.cards.append(card_one)
        enemy.card_repository.cards.append(card_two)
        self.bf.get_bonus(enemy)
        self.assertEqual(self.enemy.health, 250)

    def test_attacks_enemy_take_damage(self):
        card_one = MagicCard('b')
        card_two = TrapCard('c')
        self.attacker.card_repository.cards.append(card_one)
        self.attacker.card_repository.cards.append(card_two)
        self.bf.attacks(self.attacker, self.enemy)
        self.assertEqual(self.enemy.health, 125)

    def test_attacks_attacker_take_damage(self):
        card_one = MagicCard('b')
        self.enemy.card_repository.cards.append(card_one)
        self.bf.attacks(self.enemy, self.attacker)
        self.assertEqual(self.attacker.health, 45)

if __name__ == '__main__':
    main()
