from typing import Iterable, List
from move import Move
from players.aiplayer import AIPlayer
from players.player import Player


class CheatingAI(AIPlayer):
    def __init__(self, player_num: int, other_players: Iterable["AIPlayer"], blank_character: str) -> None:
        super().__init__(player_num, other_players, blank_character)
        ship_coords = []

    def init_name(self, player_num: int, other_players: List["AIPlayer"]) -> None:
        self.name = f"Cheating Ai {player_num}".strip()

    def get_move(self) -> "Move":
        for row in range(self.opponents[0].board.num_rows):
            for col in range(self.opponents[0].board.num_cols):
                if self.opponents[0].board.contents[row][col].contains_ship() and self.opponents[0].board.contents[row][col].has_been_fired_at == False:
                    return Move(self, row, col)
