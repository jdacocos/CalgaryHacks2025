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

# Load images with exact filenames
door1_image_path = os.path.join("assets", "images", "door", "door1.png")
door2_image_path = os.path.join("assets", "images", "door", "door2.png")
lever_image_path = os.path.join("assets", "images", "lever", "lever.png")

fire_image_path = os.path.join("assets", "images", "fire", "widefloorfire1.png")

# Load and flip door images


# Load and flip door images
if os.path.exists(door1_image_path):
    Door1OG = pygame.image.load(door1_image_path)
    Door1OG = pygame.transform.scale(Door1OG, (20, 60))
    Door1 = pygame.transform.flip(Door1OG, True, True)  # Upside down
    Door1Right = Door1OG  # Right-side up
else:
    print(f"Error: Image '{door1_image_path}' not found!")
    Door1 = Door1Right = None

if os.path.exists(door2_image_path):
    Door2 = pygame.image.load(door2_image_path)
    Door2 = pygame.transform.scale(Door2, (20, 60))
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
    pygame.Rect(1020, 330, 20, 60),
    pygame.Rect(160, 630, 20, 60),
    pygame.Rect(1020, 630, 20, 60),
]



# Lever/Button (Green)
lever_image_path = os.path.join("assets", "images","lever", "lever.png")
if os.path.exists(lever_image_path):
    LeverImage = pygame.image.load(lever_image_path)
    LeverImage = pygame.transform.scale(LeverImage, (50, 40))
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
top_rectangle = pygame.Rect(450, 190, 30, 200)  # (x, y, width, height)
platform = pygame.Rect(150, 100, 900, 600)  # (x, y, width, height)
innerplateform = pygame.Rect(160, 110, 880, 580)  # (x, y, width, height)

# Define a lever 
lever = pygame.Rect(700, 650, 50, 40)  

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

    # Draw doors with images at y=630
    for door in doors:
        if door.x == 160 and door.y == 110 and Door1:
            screen.blit(Door1, (door.x, door.y))  # Top-left (Door1 upside down)
        elif door.x == 1020 and door.y == 330 and Door1Right:
            screen.blit(Door1Right, (door.x, door.y))  # Top-right (Door1 right-side up)
        elif door.x == 160 and door.y == 630 and Door1Right:
            screen.blit(Door2, (door.x, door.y))  # Bottom-left (Door1 right-side up)
        elif door.x == 1020 and door.y == 630 and Door2:
            screen.blit(Door1Right, (door.x, door.y))  # Bottom-right (Door2)
        else:
            pygame.draw.rect(screen, ORANGE, door)

    # Draw top rectangle with Rightwall brick texture
    if RightWallBrick:
        for x in range(top_rectangle.x, top_rectangle.x + top_rectangle.width, RightWallBrick.get_width()):
            for y in range(top_rectangle.y, top_rectangle.y + top_rectangle.height, RightWallBrick.get_height()):
                screen.blit(RightWallBrick, (x, y))
    else:
        pygame.draw.rect(screen, YELLOW, top_rectangle)

    
    # Draw the lever
    if LeverImage:
        screen.blit(LeverImage, (lever.x, lever.y))
    else:
        pygame.draw.rect(screen, WHITE, lever)
    
    

    pygame.display.flip()  # Update display
pygame.quit() 
