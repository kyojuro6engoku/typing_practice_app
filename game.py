import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car properties
CAR_WIDTH, CAR_HEIGHT = 50, 80
CAR_SPEED = 5

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Game")

def draw_car(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, CAR_WIDTH, CAR_HEIGHT))

def game_loop():
    # Initial car position
    x = WIDTH // 2 - CAR_WIDTH // 2
    y = HEIGHT - CAR_HEIGHT

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Move the car based on key presses
        if keys[pygame.K_LEFT]:
            x -= CAR_SPEED
        if keys[pygame.K_RIGHT]:
            x += CAR_SPEED

        # Fill the screen with black color
        screen.fill(BLACK)

        # Draw the car
        draw_car(x, y)

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
