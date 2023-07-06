import pygame
from snake_game import settings

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((settings.SCREEN_WIDTH / 2), (settings.SCREEN_HEIGHT / 2))]
        self.direction = pygame.K_RIGHT
        self.color = settings.SNAKE_COLOR

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        if self.direction == pygame.K_UP:
            self.positions.insert(0, (cur[0], cur[1]-10))
        elif self.direction == pygame.K_DOWN:
            self.positions.insert(0, (cur[0], cur[1]+10))
        elif self.direction == pygame.K_LEFT:
            self.positions.insert(0, (cur[0]-10, cur[1]))
        elif self.direction == pygame.K_RIGHT:
            self.positions.insert(0, (cur[0]+10, cur[1]))
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], 10, 10))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(pygame.K_UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(pygame.K_DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(pygame.K_LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(pygame.K_RIGHT)

    def check_collision(self, pos):
        return pos in self.positions
