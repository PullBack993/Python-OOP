from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if self.__players:
            player_name = [p for p in self.__players if p.family_name == player.family_name][0]
            if player_name in self.__players:
                return f"Player {player.family_name} has already joined"

        self.__players.append(player)
        return f"Player {player.family_name} joined team {self.__name}"

    def remove_player(self, player_name):
        try:
            player = [p for p in self.__players if p.family_name == player_name][0]
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"
#
#         if player_name in self.__players:
#             self.__players.remove(player_name)
#
#             return player_name
#             # return f"Player: {player_name}\n" \
#             #        f"Sprint: {player_name.__sprint}\n" \
#             #        f"Dribble: {player_name.__dribble}\n" \
#             #        f"Passing: {player_name.__passing}\n" \
#             #        f"Shooting: {player_name.__shooting}"
#         return f"Player {player_name} not found"
# #
# # Player: Pall
# # Sprint: 1
# # Dribble: 3
# # Passing: 5
# # Shooting: 7
