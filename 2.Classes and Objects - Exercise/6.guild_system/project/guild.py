class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        try:
            filtered_player = [p for p in self.players if p.name == player_name][0]
            filtered_player.guild = 'Unaffiliated'
            self.players.remove(filtered_player)
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        g_info = f"Guild: {self.name}\n"
        pl_info = ''
        for pl in self.players:
            pl_info += f'{pl.player_info()}'
        return g_info + pl_info
