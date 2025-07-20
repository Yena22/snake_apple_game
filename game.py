
import pygame
import sys
# from filename import class
from apple import Apple
from snake import Snake

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apple and Snake")

# Colors
RED = (255, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

# Create objects
apple = Apple(300, 200)
snake = Snake(100, 100)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.direction = 'left'
    elif keys[pygame.K_RIGHT]:
        snake.direction = 'right'
    elif keys[pygame.K_UP]:
        snake.direction = 'up'
    elif keys[pygame.K_DOWN]:
        snake.direction = 'down'
    snake.keep_moving()

    distance = (( snake.x - apple.x)**2 +( snake.x - apple.x)**2 )**0.5
    if distance<15:
        apple.reposition()

    # Draw everything
    apple.draw(screen)
    snake.draw(screen)

    pygame.display.flip()

# Exit
pygame.quit()
sys.exit()