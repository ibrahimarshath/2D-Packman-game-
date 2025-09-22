from initialize_game import initialize_game
from Draw_board import draw_board
from Ghosts import move_ghosts
from Pacman_ import move_pacman
from pills import count_pills

def play_game():
    (game_map, ui_wall, ui_ghost, ui_hero, ui_empty,
     ui_pill, wall_color, ghost_color, pacman_color, pill_color) = initialize_game()

    game_finished = False
    win = False

    while not game_finished:
        draw_board(game_map, ui_wall, ui_ghost, ui_hero, ui_empty,
                   ui_pill, wall_color, ghost_color, pacman_color, pill_color)

        game_map, ghost_hit = move_ghosts(game_map)
        if ghost_hit:
            game_finished = True
            win = False
            break

        key = input("Move (WASD): ").lower()
        game_map, hit_ghost, moved = move_pacman(game_map, key)

        if hit_ghost:
            game_finished = True
            win = False
            break

        if count_pills(game_map) == 0:
            game_finished = True
            win = True
            break

    # Final board
    final_color = "green" if win else "red"
    draw_board(game_map, ui_wall, ui_ghost, ui_hero, ui_empty,
               ui_pill, final_color, final_color, final_color, final_color)

    print("You win! :)" if win else "You lost! :/")

if __name__ == "__main__":
    play_game()
