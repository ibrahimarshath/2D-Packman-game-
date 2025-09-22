def find_positions(game_map, char):
    positions = []
    for x in range(len(game_map)):
        for y in range(len(game_map[x])):
            if game_map[x][y] == char:
                positions.append([x, y])
    return positions
