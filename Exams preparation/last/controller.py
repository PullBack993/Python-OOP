from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, card_type: str, username: str):
        player = Beginner(username) if card_type == 'Beginner' else Advanced(username)
        self.player_repository.add(player)
        # if card_type == 'Beginner':
            # self.player_repository.add(Beginner(username))
        return f"Successfully added player of type {card_type} with username: {username}"
        # else:
        #     self.player_repository.add(Advanced(username))
        #     return f"Successfully added player of type {card_type} with username: {username}"

    def add_card(self, card_type: str, name: str):
        card = MagicCard(name) if card_type == 'Magic' else TrapCard(name)
        self.card_repository.add(card)
        # if type == "TrapCard":
        #     self.card_repository.add(TrapCard(name))
        return f"Successfully added card of type {card_type}Card with name: {name}"
        # else:
        #     self.card_repository.add(MagicCard(name))
        #     f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)  # A
        card = self.card_repository.find(card_name)  # AT
        if player and card:
            player.card_repository.add(card)  # A = AT, ....
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        btf = BattleField()
        btf.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for player in self.player_repository.players:
            result += f"Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n"
            for card in player.card_repository.cards:
                result += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return result
