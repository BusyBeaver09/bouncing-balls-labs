# Import the math, random, and Pygame libraries.
import math
import random
import pygame

# Set the window size, ball count, gravity strength, and time step.
W, H = 1000, 700
N = 100
G = 3
DT = 1 / 60

# Create the Pygame window and frame-rate clock.
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# Create random starting positions, speeds, sizes, masses, and colors.
random.seed(1)
x = [random.randrange(W) for _ in range(N)]
y = [random.randrange(H) for _ in range(N)]
vx = [random.uniform(-20, 20) for _ in range(N)]
vy = [random.uniform(-20, 20) for _ in range(N)]
r = [random.uniform(2, 4) for _ in range(N)]
m = [size * size for size in r]
colors = [
    (random.randrange(80, 256), random.randrange(80, 256), random.randrange(80, 256))
    for _ in range(N)
]

# Keep running until the window is closed.
running = True
while running:
    # Handle window events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Start each ball's acceleration at zero.
    ax = [0.0] * N
    ay = [0.0] * N

    # Calculate the gravitational pull between every pair of balls.
    for i in range(N):
        for j in range(i + 1, N):
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            d2 = max(dx * dx + dy * dy, 1)
            force = G / (d2 * math.sqrt(d2))

            ax[i] += dx * force * m[j]
            ay[i] += dy * force * m[j]
            ax[j] -= dx * force * m[i]
            ay[j] -= dy * force * m[i]

    # Apply acceleration, move the balls, and bounce off the walls.
    for i in range(N):
        vx[i] += ax[i] * DT
        vy[i] += ay[i] * DT
        x[i] += vx[i] * DT
        y[i] += vy[i] * DT

        # Reverse horizontal velocity when a ball reaches a side wall.
        if x[i] < r[i] or x[i] > W - r[i]:
            vx[i] *= -1
            x[i] = max(r[i], min(W - r[i], x[i]))

        # Reverse vertical velocity when a ball reaches the top or bottom wall.
        if y[i] < r[i] or y[i] > H - r[i]:
            vy[i] *= -1
            y[i] = max(r[i], min(H - r[i], y[i]))

    # Find overlapping balls and separate them with elastic collisions.
    for i in range(N):
        for j in range(i + 1, N):
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            d2 = dx * dx + dy * dy
            minimum = r[i] + r[j]

            # Resolve the collision only when the balls overlap.
            if 0 < d2 < minimum * minimum:
                d = math.sqrt(d2)
                nx, ny = dx / d, dy / d
                overlap = minimum - d
                x[i] -= nx * overlap / 2
                y[i] -= ny * overlap / 2
                x[j] += nx * overlap / 2
                y[j] += ny * overlap / 2

                # Exchange velocity along the collision direction.
                speed = (vx[j] - vx[i]) * nx + (vy[j] - vy[i]) * ny
                if speed < 0:
                    impulse = 2 * speed / (m[i] + m[j])
                    vx[i] += impulse * m[j] * nx
                    vy[i] += impulse * m[j] * ny
                    vx[j] -= impulse * m[i] * nx
                    vy[j] -= impulse * m[i] * ny

    # Clear the screen and draw every ball.
    screen.fill((10, 15, 30))
    for i in range(N):
        pygame.draw.circle(screen, colors[i], (round(x[i]), round(y[i])), round(r[i]))

    # Show the new frame and maintain 60 frames per second.
    pygame.display.flip()
    clock.tick(60)

# Shut down Pygame after the window closes.
pygame.quit()
