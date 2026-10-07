import pygame
import random

# Initialization & window setup
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Sample")
clock = pygame.time.Clock()

# Variables and state setup
x, y = 300.0, 200.0
dx, dy = 4.0, 3.0
radius = 24
gravity = 0.15
friction = 0.9
circle_color = (233, 30, 99)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    dy += gravity
    x += dx
    y += dy

    # Horizontal bounce
    if x - radius < 0:
        x = radius
        dx = abs(dx)
        circle_color = tuple(random.randint(0, 255) for _ in range(3))
    elif x + radius > WIDTH:
        x = WIDTH - radius
        dx = -abs(dx)
        circle_color = tuple(random.randint(0, 255) for _ in range(3))

    # Vertical bounce with energy loss
    if y + radius > HEIGHT:
        y = HEIGHT - radius
        dy = -abs(dy) * friction
        dx *= friction
        circle_color = tuple(random.randint(0, 255) for _ in range(3))
    elif y - radius < 0:
        y = radius
        dy = abs(dy) * friction
        circle_color = tuple(random.randint(0, 255) for _ in range(3))

    # Rendering
    screen.fill((20, 24, 40))
    pygame.draw.circle(screen, circle_color, (round(x), round(y)), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
