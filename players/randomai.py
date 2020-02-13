from typing import Iterable, List
import move
from board import Board
from cell import Cell
import random
from players.aiplayer import AIPlayer


class RandomAI(AIPlayer):
    def __init__(self, player_num: int, other_players: Iterable["AIPlayer"], blank_character: str) -> None:
        super().__init__(player_num, other_players, blank_character)
        self.ship_coords = []
        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                self.ship_coords.append((row, col))

    def init_name(self, player_num: int, other_players: List["AIPlayer"]) -> None:
        self.name = f"Random AI {player_num}".strip()

    def get_move(self) -> move.Move:
        coord = random.choice(self.ship_coords)
        self.ship_coords.remove(coord)
        return move.Move(self, *coord)
