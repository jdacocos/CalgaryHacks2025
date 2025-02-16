import pygame, os

from character import Character
from audio import play_background_music, stop_background_music, play_sound


# Pygame setup
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

image_path = os.path.join("assets", "images", "Bricks", "FloorBrick.png")
if os.path.exists(image_path):
    FloorBrick = pygame.image.load(image_path)
else:
    print(f"Error: Image '{image_path}' not found!")
    FloorBrick = None

# Define a rectangle (platform)
platform = pygame.Rect(150, 100 ,900, 600)  # (x, y, width, height)
innerplateform = pygame.Rect(160, 110, 880, 580)  # (x, y, width, height)

# Character Sprites
blue_dino = {
    "idle": "./character/doux_frame_01.png",
    "walk": "./character/doux_frame_21.png",
    "jump": "./character/doux_frame_11.png"
}

red_dino = {
    "idle": "./character/frame_00.png",
    "walk": "./character/frame_21.png",
    "jump": "./character/frame_11.png"
}

# Create Players
player1 = Character(400, 648, blue_dino, {
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d
}, SCREEN_WIDTH)

player2 = Character(400, 348, red_dino, {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT
}, SCREEN_WIDTH)

play_background_music()

# Game Loop
while running:
    screen.fill(WHITE)  # Clear screen

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

    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pass events to character movement handling
        player1.handle_event(event)
        player2.handle_event(event)

    # Update player movement
    player1.move()
    player2.move()

    # Draw players
    player1.draw(screen)
    player2.draw(screen)

    #ADD THE "COVER" here, like cover for "beyond the walls" so it we dont see "teleport". Just so it goes "over top of character".

    # Flip display
    pygame.display.flip()
    clock.tick(60)  # Cap frame rate at 60 FPS

pygame.quit()
