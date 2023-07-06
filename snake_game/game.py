import pygame
from snake_game.snake import Snake
from snake_game.food import Food
from snake_game.settings import Settings

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.snake = Snake(self)
        self.food = Food(self)
        self.score = 0
        self.is_game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    self.snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = 'RIGHT'

    def update(self):
        if not self.is_game_over:
            self.snake.update()
            self.check_collision()

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.snake.draw()
        self.food.draw()
        pygame.display.flip()

    def check_collision(self):
        if self.snake.check_collision_with_self() or self.snake.check_collision_with_boundaries():
            self.is_game_over = True
        elif self.snake.check_collision_with_food(self.food):
            self.snake.grow()
            self.food = Food(self)
            self.score += 1
