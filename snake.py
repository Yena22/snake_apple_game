import pygame
# Snake class

RED = (255, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)


class Snake:
    def __init__(self, x, y, width=20, height=20, speed=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = 'right'

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

    def keep_moving(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

   
        
        