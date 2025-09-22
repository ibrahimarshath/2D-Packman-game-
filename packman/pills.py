def count_pills(game_map):
    return sum(row.count('P') for row in game_map)
