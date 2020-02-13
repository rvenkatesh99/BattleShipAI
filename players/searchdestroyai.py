from typing import List, Iterable
from players.aiplayer import AIPlayer
from players.randomai import RandomAI
import move
import random


class SearchDestroyAI(AIPlayer):
    def __init__(self, player_num: int, other_players: Iterable["AIPlayer"], blank_character: str) -> None:
        super().__init__(player_num, other_players, blank_character)
        self.shoot_coords = []
        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                self.shoot_coords.append((row, col))
        self.destroy_coords = []

    def init_name(self, player_num: int, other_players: List["AIPlayer"]) -> None:
        self.name = f"Search Destroy AI {player_num}".strip()

    def get_move(self) -> move.Move:
        coord = random.choice(self.shoot_coords)
        row = coord[0]
        col = coord[1]
        if self.opponents[0].board.contents[row][col].contains_ship():
            for row in range(self.opponents[0].board.num_rows):
                for col in range(self.opponents[0].board.num_cols):
                    try:
                        self.destroy_coords.append((row, col -1))
                        self.destroy_coords.append((row-1, col))
                        self.destroy_coords.append((row, col+1))
                        self.destroy_coords.append((row+1, col))
                    except:
                        continue
        shoot_coord = self.destroy_coords[0]
        shoot_coord.remove(shoot_coord)
        return move.Move(self, *shoot_coord)
