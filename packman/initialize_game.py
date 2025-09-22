import random
from termcolor import colored


def initialize_game():
    game_map = [
        "|--------|",
        "|G..|..G.|",
        "|...PP...|",
        "|G....@|.|",
        "|...P..|.|",
        "|--------|"
    ]

    
    ui_wall = ["......", "......", "......", "......"]
    ui_ghost = [" .-.  ", "| OO| ", "|   | ", "'^^^' "]
    ui_hero = [" .--. ", "/ _.-'", "\\  '-.", " '--' "]
    ui_empty = ["      ", "      ", "      ", "      "]
    ui_pill = ["      ", " .-.  ", " '-'  ", "      "]

    wall_color = "blue"
    ghost_color = "red"
    pacman_color = "yellow"
    pill_color = "grey"

    return (game_map, ui_wall, ui_ghost, ui_hero, ui_empty,
            ui_pill, wall_color, ghost_color, pacman_color, pill_color)