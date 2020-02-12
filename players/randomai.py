from typing import Iterable, List
import move
import random
from players.aiplayer import AIPlayer


class RandomAI(AIPlayer):
    def __init__(self, player_num: int, other_players: Iterable["AIPlayer"], blank_character: str) -> None:
        super().__init__(player_num, other_players, blank_character)

    def init_name(self, player_num: int, other_players: List["AIPlayer"]) -> None:
        self.name = f"Random AI {player_num}".strip()

    def get_move(self) -> move.Move:
        ship_coords = []
        for row in range(self.board.get_display(hidden=True).num_rows):
            for col in range(self.board.get_display(hidden=True).num_cols):
                if self.board.get_display(hidden=True)[row][col] == self.board.blank_char:
                    ship_coords.append((row,col))

        coord = random.choice(ship_coords)
        ship_coords.remove(coord)
        return move.Move(self, *coord)
