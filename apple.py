import pygame
import random

RED = (255, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

# Apple class
class Apple:
    def __init__(self, x, y, radius=10):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def reposition(self):
        self.x =random.randint(0,600)
        self.y = random.randint(0,400)
