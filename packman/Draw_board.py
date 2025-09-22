from termcolor import colored

def draw_board(game_map, ui_wall, ui_ghost, ui_hero, ui_empty, ui_pill,
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
