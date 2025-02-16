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
ORANGE = (255, 165, 0)  # Doors
RED = (255, 0, 0)      # Fire/Traps
BLUE = (0, 0, 255)      # Floating Platforms
GREEN = (0, 255, 0)    # Lever/Button
YELLOW = (255, 255, 0)  # Additional elements (new rectangles)

# Load images with exact filenames
floor_image_path = os.path.join("assets", "images", "Bricks", "FloorBrick.png")
roof_image_path = os.path.join("assets", "images", "Bricks", "RoofBrick.png")
left_wall_image_path = os.path.join("assets", "images", "Bricks", "Leftwall brick.png")
right_wall_image_path = os.path.join("assets", "images", "Bricks", "Rightwall brick.png")

door1_image_path = os.path.join("assets", "images", "door", "door1.png")
door2_image_path = os.path.join("assets", "images", "door", "door2.png")

fire_image_path = os.path.join("assets", "images", "fire", "widefloorfire1.png")

# Load and flip door images
if os.path.exists(door1_image_path):
    Door1OG = pygame.image.load(door1_image_path)
    Door1OG = pygame.transform.scale(Door1OG, (20, 60))
    Door1 = pygame.transform.flip(Door1OG, False, True)  # Flip the image upside down
else:
    print(f"Error: Image '{door1_image_path}' not found!")
    Door1 = None

if os.path.exists(door2_image_path):
    Door2 = pygame.image.load(door2_image_path)
    Door2 = pygame.transform.scale(Door2, (20, 60))
    Door2 = pygame.transform.flip(Door2, False, True)  # Flip the image upside down
else:
    print(f"Error: Image '{door2_image_path}' not found!")
    Door2 = None

# Load fire image
if os.path.exists(fire_image_path):
    FireImage = pygame.image.load(fire_image_path)
    FireImage = pygame.transform.scale(FireImage, (50, 25))  # Resize to match trap size
    FireImageFlipped = pygame.transform.flip(FireImage, False, True)  # Flip the image upside down
else:
    print(f"Error: Image '{fire_image_path}' not found!")
    FireImage = None
    FireImageFlipped = None

# Load FloorBrick texture
if os.path.exists(floor_image_path):
    FloorBrick = pygame.image.load(floor_image_path)
    FloorBrickFlipped = pygame.transform.flip(FloorBrick, False, True)  # Flip upside down for specific platforms
else:
    print(f"Error: Image '{floor_image_path}' not found!")
    FloorBrick = None
    FloorBrickFlipped = None

# Doors (Orange)
doors = [
    pygame.Rect(160, 110, 20, 60),
    pygame.Rect(1020, 110, 20, 60),
    pygame.Rect(160, 418, 20, 60),
    pygame.Rect(1020, 630, 20, 60),
]

# Fire/Traps (Red)
traps = [
    pygame.Rect(350, 110, 500, 15),
    pygame.Rect(350, 420, 500, 15),
    pygame.Rect(160, 670, 750, 15),
]

floating_platforms_list = [
    pygame.Rect(250, 500, 200, 20),
    pygame.Rect(550, 500, 200, 20),
    pygame.Rect(400, 600, 200, 20),
    pygame.Rect(700, 600, 200, 20),
]

# Lever/Button (Green)
lever_image_path = os.path.join("assets", "images","lever", "lever.png")
if os.path.exists(lever_image_path):
    LeverImage = pygame.image.load(lever_image_path)
    LeverImage = pygame.transform.scale(LeverImage, (40, 30))
else:
    print(f"Error: Image '{lever_image_path}' not found!")
    LeverImage = None
lever = pygame.Rect(820, 580, 50, 20)


# Load FloorBrick
if os.path.exists(floor_image_path):
    FloorBrick = pygame.image.load(floor_image_path)
else:
    print(f"Error: Image '{floor_image_path}' not found!")
    FloorBrick = None

# Load RoofBrick
if os.path.exists(roof_image_path):
    RoofBrick = pygame.image.load(roof_image_path)
else:
    print(f"Error: Image '{roof_image_path}' not found!")
    RoofBrick = None

# Load Left Wall Brick
if os.path.exists(left_wall_image_path):
    LeftWallBrick = pygame.image.load(left_wall_image_path)
else:
    print(f"Error: Image '{left_wall_image_path}' not found!")
    LeftWallBrick = None

# Load Right Wall Brick
if os.path.exists(right_wall_image_path):
    RightWallBrick = pygame.image.load(right_wall_image_path)
else:
    print(f"Error: Image '{right_wall_image_path}' not found!")
    RightWallBrick = None

# Define a rectangle (platform)
platform = pygame.Rect(150, 100, 900, 600)  # (x, y, width, height)
innerplateform = pygame.Rect(160, 110, 880, 580)  # (x, y, width, height)

# Game loop
running = True
while running:
    screen.fill(BLACK)  # Fill the entire screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the outer rectangle (platform)
    pygame.draw.rect(screen, BLACK, platform)  # Keep platform black

    # Draw the inner rectangle in white
    pygame.draw.rect(screen, WHITE, innerplateform)
    
    # Draw the brick images along all four lines and two walls if loaded
    if FloorBrick and RoofBrick and LeftWallBrick and RightWallBrick:
        floor_width, floor_height = FloorBrick.get_size()
        roof_width, roof_height = RoofBrick.get_size()
        left_wall_width, left_wall_height = LeftWallBrick.get_size()
        right_wall_width, right_wall_height = RightWallBrick.get_size()
        
        # Topmost line (platform top edge) -> **Use RoofBrick**
        for x in range(150, 1050, roof_width):
            screen.blit(RoofBrick, (x, platform.top - (roof_height // 2)))  

        # Bottommost line (platform bottom edge) -> **Use FloorBrick**
        for x in range(150, 1050, floor_width):
            screen.blit(FloorBrick, (x, platform.bottom - (floor_height // 2)))  

        # Middle-top line (upper center line) -> **Use FloorBrick**
        for x in range(150, 1050, floor_width):
            screen.blit(FloorBrick, (x, platform.centery - 10))  

        # Middle-bottom line (lower center line) -> **Use RoofBrick**
        for x in range(150, 1050, roof_width):
            screen.blit(RoofBrick, (x, platform.centery + 5))  

        # Left wall (left edge) -> **Use Leftwall brick**
        for y in range(100, 700, left_wall_height):
            screen.blit(LeftWallBrick, (platform.left - (left_wall_width // 2), y))  

        # Right wall (right edge) -> **Use Rightwall brick**
        for y in range(100, 700, right_wall_height):
            screen.blit(RightWallBrick, (platform.right - (right_wall_width // 2), y))  
    # Draw doors
    for door in doors:
        if door.x == 160 and Door2:
            screen.blit(Door2, (door.x, door.y))
        elif door.x == 1020 and Door1:
            screen.blit(Door1, (door.x, door.y))
        else:
            pygame.draw.rect(screen, ORANGE, door)

        # Draw doors with images at y=630
    for door in doors:
        if door.y == 630 and Door1:
            screen.blit(Door1OG, (door.x, door.y))

    # Draw floating platforms with FloorBrick texture
    
        # Draw fire/traps
    for trap in traps:
        if trap.x == 350 and FireImageFlipped:
            for x in range(trap.x, trap.x + trap.width, FireImageFlipped.get_width()):
                screen.blit(FireImageFlipped, (x, trap.y))
            screen.blit(FireImageFlipped, (trap.x, trap.y))
        elif trap.x == 160 and FireImage:
            for x in range(trap.x, trap.x + trap.width, FireImage.get_width()):
                screen.blit(FireImage, (x, trap.y))
            screen.blit(FireImage, (trap.x, trap.y))
        else:
            pygame.draw.rect(screen, RED, trap)

    # Draw floating platforms with FloorBrick texture
    for floatingPlatform in floating_platforms_list:
        if floatingPlatform.y == 500 and FloorBrickFlipped:
            for x in range(floatingPlatform.x, floatingPlatform.x + floatingPlatform.width, FloorBrickFlipped.get_width()):
                screen.blit(FloorBrickFlipped, (x, floatingPlatform.y))
        elif FloorBrick:
            for x in range(floatingPlatform.x, floatingPlatform.x + floatingPlatform.width, FloorBrick.get_width()):
                screen.blit(FloorBrick, (x, floatingPlatform.y))

            # Draw lever/button
    if LeverImage:
        screen.blit(LeverImage, (lever.x, lever.y))
    else:
        pygame.draw.rect(screen, GREEN, lever)
    
    pygame.display.flip()  # Update display
pygame.quit() 
