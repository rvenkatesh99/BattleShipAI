from typing import Iterable, List
from move import Move
from players.aiplayer import AIPlayer


class CheatingAI(AIPlayer):
    def __init__(self, player_num: int, other_players: Iterable["AIPlayer"], blank_character: str) -> None:
        super().__init__(player_num, other_players, blank_character)

    def init_name(self, player_num: int, other_players: List["AIPlayer"]) -> None:
        self.name = f"Cheating AI {player_num}".strip()

    def get_move(self) -> "Move":
        ship_coords = ""
        opponent = AIPlayer.opponents[0]
        for row in range(opponent.board.num_rows):
            for col in range(opponent.board.num_cols):
                if self[row][col] != self.board.blank_character and self[row][col] != 'X' and self[row][col] != 'O':
                    ship_coords = f"{row},{col}"
                try:
                    firing_location = Move.from_str(self, ship_coords)
                except ValueError as e:
                    print(e)
                    continue
                return firing_location
