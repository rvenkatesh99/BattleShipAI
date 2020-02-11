from typing import Iterable, List
from board import Board
from move import Move
from ship import Ship
from orientation import Orientation
from players.player import Player
import random


class AIPlayer(Player):
    def __init__(self, player_num: int, other_players: Iterable["Player"], blank_character: str) -> None:
        super().__init__(other_players, blank_character)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        ...

    def place_ship(self, ship_: Ship) -> None:
        while True:
            placement = self.get_ship_placement(ship_)
            try:
                self.board.place_ship(placement)
            except ValueError as e:
                pass
            else:
                return

    def get_ship_orientation(self, ship_: Ship) -> Orientation:
        return random.choice([Orientation.HORIZONTAL, Orientation.VERTICAL])

    def get_ship_start_coords(self, ship_: Ship, orientation_: Orientation):

        if orientation_ == Orientation.HORIZONTAL:
            row = random.randint(0, self.board.num_rows - 1)
            col = random.randint(0, self.board.num_cols - ship_.length)
        else:
            row = random.randint(0, self.board.num_rows - ship_.length)
            col = random.randint(0, self.board.num_cols - 1)
        return row, col

    def get_move(self, the_board: Board) -> "Move":
        empty_coordinates = the_board.get_empty_coordinates()
        coord = random.choice(empty_coordinates)
        return Move(self, *coord)