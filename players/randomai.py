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
        opponent = AIPlayer.opponents[0]
        ship_coords = ""
        while True:
            for row in range(opponent.board.num_rows):
                row_choice = random.choice(row)
                for col in range(opponent.board.num_cols):
                    col_choice = random.choice(col)

                    ship_coords = f"{row_choice},{col_choice}"
            try:
                firing_location = move.Move.from_str(self, ship_coords)
            except ValueError as e:
                print(e)
                continue
            return firing_location
