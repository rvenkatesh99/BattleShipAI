import sys
import game

if __name__ == '__main__':
    seed = None

    if len(sys.argv) >= 3:
        seed = int(sys.argv[2])

    if len(sys.argv) < 2:
        print('Not enough arguments given.')
    else:
        game_of_battle_ship = game.Game(sys.argv[1]) #Create game
        game_of_battle_ship.play() # Play it