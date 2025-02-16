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
LIGHTBLUE = (173, 216, 230)

# Load images with correct path handling
def load_image(path, size):
    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)  # Resize image
    except pygame.error:
        print(f"Error: Image '{path}' not found!")
        return None

# Load brick textures
FloorBrick = load_image(os.path.join("assets", "images", "Bricks", "FloorBrick.png"), (30, 20))
RoofBrick = load_image(os.path.join("assets", "images", "Bricks", "roofBrick.png"), (30, 20))
LeftBrick = load_image(os.path.join("assets", "images", "Bricks", "Leftwall Brick.png"), (30, 20))
RightBrick = load_image(os.path.join("assets", "images", "Bricks", "Rightwall Brick.png"), (30, 20))
Door1 = load_image(os.path.join("assets", "images", "door", "door1.png"), (30, 80))


# Define platform rectangles
platform = pygame.Rect(150, 100, 900, 600)  # Outer platform
inner_platform = pygame.Rect(160, 110, 880, 580)  # Inner platform

def draw_brick_line(y_pos):
    """Draws thinner bricks along the given y position."""
    if FloorBrick:
        brick_width, _ = FloorBrick.get_size()
        for x in range(150, 1050, brick_width):
            screen.blit(FloorBrick, (x, y_pos))

def draw_roof_line(y_pos):
    if RoofBrick:
        brick_width, _ = RoofBrick.get_size()
        for x in range(150, 1050, brick_width):
            screen.blit(RoofBrick, (x, y_pos))

def draw_left_line(x_pos):
    if LeftBrick:
        _, brick_height = LeftBrick.get_size()
        for y in range(100, 700, brick_height):
            screen.blit(LeftBrick, (x_pos, y))

def draw_right_line(x_pos):
    if RightBrick:
        _, brick_height = RightBrick.get_size()
        for y in range(100, 700, brick_height):
            screen.blit(RightBrick, (x_pos, y))

def draw_door(x_pos, y_pos):
    """Draws the door on the right wall."""
    if Door1:
        screen.blit(Door1, (x_pos, y_pos))

# Game loop
running = True
while running:
    screen.fill(BLUE)  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the outer and inner platforms
    pygame.draw.rect(screen, BLACK, platform)
    pygame.draw.rect(screen, LIGHTBLUE, inner_platform)

    # Draw a middle line (split into two thinner lines for a gap effect)
   # pygame.draw.line(screen, BLACK, (150, platform.centery - 5), (1050, platform.centery - 5), 10)
   # pygame.draw.line(screen, BLACK, (150, platform.centery + 5), (1050, platform.centery - 6), 10)

    # Draw thinner bricks along the top and bottom of the platform
    draw_brick_line(platform.centery - 25)
    draw_brick_line(platform.centery + 280)

    # Draw roof and side walls
    draw_roof_line(platform.centery -10)
    draw_roof_line(platform.top - 10)
    draw_left_line(platform.left)
    draw_right_line(platform.right - 30)
    draw_door(platform.right - 55, platform.centery - 100)  # Positioned at the center of the right wall
    draw_door(platform.right - 55, platform.bottom - 95)  # Positioned at the center of the right wall, adjusted for new size


    pygame.display.flip()  # Update display

pygame.quit()
