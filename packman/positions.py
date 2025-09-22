from termcolor import colored
from initialize_game import initialize_game
from Draw_board import draw_board
from Ghosts import move_ghosts
from Pacman_ import move_pacman
from pills import count_pills
from positions import find_positions

def find_positions(game_map, char):
    positions = []
    for x in range(len(game_map)):
        for y in range(len(game_map[x])):
            if game_map[x][y] == char:
                positions.append([x, y])
    return positions