from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        if any(p.username == player.username for p in self.players):
        # if self.find(player.username):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        ply = self.find(player)
        self.players.remove(ply)

    def find(self, username: str):
        for player in self.players:
            if player.username == username:
                return player
