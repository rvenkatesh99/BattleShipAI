from typing import Iterable
from players.player import Player

class HumanPlayer(Player):

    def __init__(self, other_players: Iterable["Player"], blank_character: str) -> None:
        super().__init__(other_players, blank_character)

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')