from termcolor import colored
from initialize_game import initialize_game
from Draw_board import draw_board
from Ghosts import move_ghosts
from Pacman_ import move_pacman
from pills import count_pills
from positions import find_positions

def move_pacman(game_map, key):
    pacman = find_positions(game_map, '@')[0]
    px, py = pacman
    nx, ny = px, py

    if key == 'a':
        ny -= 1
    elif key == 's':
        nx += 1
    elif key == 'w':
        nx -= 1
    elif key == 'd':
        ny += 1
    else:
        return game_map, False, False

    if nx < 0 or nx >= len(game_map) or ny < 0 or ny >= len(game_map[0]):
        return game_map, False, False

    target = game_map[nx][ny]
    if target in ['|', '-']:
        return game_map, False, False
    if target == 'G':
        return game_map, True, False

    # Move pacman
    game_map[px] = game_map[px][:py] + "." + game_map[px][py + 1:]
    game_map[nx] = game_map[nx][:ny] + "@" + game_map[nx][ny + 1:]

    return game_map, False, True