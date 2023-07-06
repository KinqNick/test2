import pygame
import random
from snake_game.settings import Settings

class Food:
    def __init__(self):
        self.settings = Settings()
        self.position = [random.randrange(1, self.settings.window_width/10)*10, random.randrange(1, self.settings.window_height/10)*10]
        self.food_spawn = True

    def draw_food(self, surface):
        pygame.draw.rect(surface, self.settings.food_color, pygame.Rect(self.position[0], self.position[1], self.settings.block_size, self.settings.block_size))

    def spawn_food(self):
        if self.food_spawn == False:
            self.position = [random.randrange(1, self.settings.window_width/10)*10, random.randrange(1, self.settings.window_height/10)*10]
        self.food_spawn = True