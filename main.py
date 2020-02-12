import sys
import game

if __name__ == '__main__':
    seed = None

    if len(sys.argv) < 2:
        print('Not enough arguments given.')

    if len(sys.argv) >= 3:
        seed = int(sys.argv[2])

    game_of_battle_ship = game.Game(sys.argv[1], seed) #Create game
    game_of_battle_ship.play() # Play it