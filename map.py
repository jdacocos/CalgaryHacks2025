import pygame
import os

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Rectangle Map")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Load image with correct path handling
image_path = os.path.join("assets", "images", "Bricks", "FloorBrick.png")
if os.path.exists(image_path):
    FloorBrick = pygame.image.load(image_path)
else:
    print(f"Error: Image '{image_path}' not found!")
    FloorBrick = None

# Define a rectangle (platform)
platform = pygame.Rect(150, 100 ,900, 600)  # (x, y, width, height)
innerplateform = pygame.Rect(160, 110, 880, 580)  # (x, y, width, height)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the rectangle (platform)
    pygame.draw.rect(screen, BLACK, platform)

    # Draw the inner rectangle
    pygame.draw.rect(screen, WHITE, innerplateform)
    
    # Draw a line in the middle
    pygame.draw.line(screen, BLACK, (150, platform.centery -5), (1040, platform.centery -5), 10)
    pygame.draw.line(screen, BLACK, (150, platform.centery +5), (1040, platform.centery +5), 10)

    # Draw the image repeatedly along the top line if it exists
    if FloorBrick:
        brick_width, brick_height = FloorBrick.get_size()
        for x in range(150, 1050, brick_width):
            screen.blit(FloorBrick, (x, platform.centery - 10))  # Align the image with the top line

    pygame.display.flip()  # Update display

pygame.quit()
