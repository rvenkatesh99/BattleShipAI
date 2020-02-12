from typing import Iterable, List
from move import Move
from players.aiplayer import AIPlayer
from players.player import Player

class CheatingAI(AIPlayer):
    def __init__(self, player_num: int, other_players: Iterable["AIPlayer"], blank_character: str) -> None:
        super().__init__(player_num, other_players, blank_character)

    def init_name(self, player_num: int, other_players: List["AIPlayer"]) -> None:
        self.name = f"Cheating AI {player_num}".strip()

    def get_move(self) -> "Move":
        ship_coords = []
        opponent = AIPlayer.other_players[0]
        for row in range(opponent.board.num_rows):
            for col in range(opponent.board.num_cols):
                if opponent.board[row][col] != opponent.board.blank_character and opponent.board[row][col] != 'X':
                    ship_coords.append((row, col))

        coord = ship_coords[0]
        ship_coords.remove(coord)
        return Move(self, *coord)
