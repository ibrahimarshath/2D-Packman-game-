from termcolor import colored
from initialize_game import initialize_game
from Draw_board import draw_board
from Ghosts import move_ghosts
from Pacman_ import move_pacman
from pills import count_pills
from positions import find_positions

def count_pills(game_map):
    return sum(row.count('P') for row in game_map)

