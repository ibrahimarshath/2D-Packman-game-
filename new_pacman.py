import random
from termcolor import colored


class GameInitializer:
    def __init__(self):
        pass
    
    def initialize_game(self):
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


class BoardRenderer:
    def __init__(self):
        pass
    
    def draw_board(self, game_map, ui_wall, ui_ghost, ui_hero, ui_empty, ui_pill,
                   wall_color, ghost_color, pacman_color, pill_color):
        for row in game_map:
            for piece in range(4):
                for point in row:
                    if point == 'G':
                        print(colored(ui_ghost[piece], ghost_color), end='')
                    elif point in ['|', '-']:
                        print(colored(ui_wall[piece], wall_color), end='')
                    elif point == '@':
                        print(colored(ui_hero[piece], pacman_color), end='')
                    elif point == '.':
                        print(ui_empty[piece], end='')
                    elif point == 'P':
                        print(colored(ui_pill[piece], pill_color), end='')
                print("", end='\n')


class PositionFinder:
    def __init__(self):
        pass
    
    def find_positions(self, game_map, char):
        positions = []
        for x in range(len(game_map)):
            for y in range(len(game_map[x])):
                if game_map[x][y] == char:
                    positions.append([x, y])
        return positions


class Ghost:
    def __init__(self, position_finder):
        self.position_finder = position_finder
    
    def move_ghosts(self, game_map):
        all_ghosts = self.position_finder.find_positions(game_map, 'G')
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


class Pacman:
    def __init__(self, position_finder):
        self.position_finder = position_finder
    
    def move_pacman(self, game_map, key):
        pacman = self.position_finder.find_positions(game_map, '@')[0]
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

        game_map[px] = game_map[px][:py] + "." + game_map[px][py + 1:]
        game_map[nx] = game_map[nx][:ny] + "@" + game_map[nx][ny + 1:]

        return game_map, False, True


class PillCounter:
    def __init__(self):
        pass
    
    def count_pills(self, game_map):
        return sum(row.count('P') for row in game_map)


def play_game():
    game_initializer = GameInitializer()
    board_renderer = BoardRenderer()
    position_finder = PositionFinder()
    ghost = Ghost(position_finder)
    pacman = Pacman(position_finder)
    pill_counter = PillCounter()
    
    (game_map, ui_wall, ui_ghost, ui_hero, ui_empty,
     ui_pill, wall_color, ghost_color, pacman_color, pill_color) = game_initializer.initialize_game()

    game_finished = False
    win = False

    while not game_finished:
        board_renderer.draw_board(game_map, ui_wall, ui_ghost, ui_hero, ui_empty,
                   ui_pill, wall_color, ghost_color, pacman_color, pill_color)

        game_map, ghost_hit = ghost.move_ghosts(game_map)
        if ghost_hit:
            game_finished = True
            win = False
            break

        key = input("Move (WASD): ").lower()
        game_map, hit_ghost, moved = pacman.move_pacman(game_map, key)

        if hit_ghost:
            game_finished = True
            win = False
            break

        if pill_counter.count_pills(game_map) == 0:
            game_finished = True
            win = True
            break

    final_color = "green" if win else "red"
    board_renderer.draw_board(game_map, ui_wall, ui_ghost, ui_hero, ui_empty,
               ui_pill, final_color, final_color, final_color, final_color)

    print("You win! :)" if win else "You lost! :/")

if __name__ == "__main__":
    play_game()
