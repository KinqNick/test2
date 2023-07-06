import pygame
from snake_game.game import Game
from snake_game.settings import Settings

def main():
    pygame.init()
    settings = Settings()
    game = Game(settings)

    while not game.is_game_over:
        game.handle_events()
        game.update()
        game.draw()

    pygame.quit()

if __name__ == "__main__":
    main()