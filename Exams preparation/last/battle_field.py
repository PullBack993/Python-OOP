from project.player.player import Player


class BattleField:

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == 'Beginner':
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == 'Beginner':
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        self.get_bonus(attacker)
        self.get_bonus(enemy)
        self.attacks(attacker, enemy)
        self.attacks(enemy, attacker)

    @staticmethod
    def get_bonus(player):
        player.health += sum([card.health_points for card in player.card_repository.cards])

    @staticmethod
    def attacks(attacker: Player, attacked: Player):
        for card in attacker.card_repository.cards:
            attacked.take_damage(card.damage_points)
