import random
from positions import find_positions

def move_ghosts(game_map):
    all_ghosts = find_positions(game_map, 'G')
    game_finished = False

    for ghost in all_ghosts:
        old_x, old_y = ghost
        possible_directions = [
            [old_x, old_y + 1],
            [old_x + 1, old_y],
            [old_x, old_y - 1],
            [old_x - 1, old_y]
        ]
        nx, ny = random.choice(possible_directions)

        if nx < 0 or nx >= len(game_map) or ny < 0 or ny >= len(game_map[0]):
            continue

        target = game_map[nx][ny]
        if target in ['|', '-', 'G']:
            continue
        if target == '@':
            game_finished = True
        else:
            game_map[old_x] = game_map[old_x][:old_y] + "." + game_map[old_x][old_y + 1:]
            game_map[nx] = game_map[nx][:ny] + "G" + game_map[nx][ny + 1:]

    return game_map, game_finished
