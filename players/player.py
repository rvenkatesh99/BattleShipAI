from typing import Dict, List
import copy
import ship_placement
import ship
import orientation
import move
import game_config
import board
from firing_location_error import FiringLocationError

import abc


class Player(abc.ABC):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__()
        self.name = 'No Name'
        self.init_name(player_num, other_players)
        self.board = board.Board(config)
        self.opponents = other_players[:]  # a copy of other players
        self.ships = copy.deepcopy(config.available_ships)
        self.place_ships()

        # make this player the opponent of all the other players
        for opponent in other_players:
            opponent.add_opponent(self)

    @abc.abstractmethod
    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        ...

    def add_opponent(self, opponent: "Player") -> None:
        self.opponents.append(opponent)

    def place_ships(self) -> None:
        for ship_ in self.ships.values():
            self.display_placement_board()
            self.place_ship(ship_)
        self.display_placement_board()

    @abc.abstractmethod
    def place_ship(self, ship_: ship.Ship) -> None:
        ...

    def get_ship_placement(self, ship_: ship.Ship):
        while True:
            try:
                orientation_ = self.get_orientation(ship_)
                start_row, start_col = self.get_start_coords(ship_)
            except ValueError as e:
                print(e)
            else:
                return ship_placement.ShipPlacement(ship_, orientation_, start_row, start_col)

    @abc.abstractmethod
    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        ...

    @abc.abstractmethod
    def get_start_coords(self, ship_: ship.Ship):
        ...

    def all_ships_sunk(self) -> bool:
        return all(ship_.health == 0 for ship_ in self.ships.values())

    def get_move(self) -> move.Move:
        while True:
            coords = input(f'{self.name}, enter the location you want to fire at in the form row, column: ')
            try:
                firing_location = move.Move.from_str(self, coords)
            except ValueError as e:
                print(e)
                continue
            return firing_location

    def fire_at(self, row: int, col: int) -> None:
        opponent = self.opponents[0]
        if not opponent.board.coords_in_bounds(row, col):
            raise FiringLocationError(f'{row}, {col} '
                                      f'is not in bounds of our '
                                      f'{opponent.board.num_rows} X {opponent.board.num_cols} board.')
        elif opponent.board.has_been_fired_at(row, col):
            raise FiringLocationError(f'You have already fired at {row}, {col}.')
        else:
            opponent.receive_fire_at(row, col)
            self.display_scanning_boards()
            self.display_firing_board()

    def receive_fire_at(self, row: int, col: int) -> None:
        location_fired_at = self.board.shoot(row, col)
        if location_fired_at.contains_ship():
            ship_hit = self.ships[location_fired_at.content]
            ship_hit.damage()
            print(f"You hit {self.name}'s {ship_hit}!")
            if ship_hit.destroyed():
                print(f"You destroyed {self.name}'s {ship_hit}")
        else:
            print('Miss')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return False
        else:
            return self.name == other.name

    def __ne__(self, other: object) -> bool:
        return self != other

    def display_placement_board(self) -> None:
        print(f"{self.name}'s Placement Board")
        print(self.get_visible_representation_of_board(), end='')

    def display_scanning_boards(self) -> None:
        print(f"{self.name}'s Scanning Board")
        for opponent in self.opponents:
            print(opponent.get_hidden_representation_of_board(), end='')

    def display_firing_board(self) -> None:
        print(f"\n{self.name}'s Board")
        print(self.get_visible_representation_of_board())

    def get_hidden_representation_of_board(self) -> str:
        return self.board.get_display(hidden=True)

    def get_visible_representation_of_board(self) -> str:
        return self.board.get_display(hidden=False)

    def __str__(self) -> str:
        return self.name

