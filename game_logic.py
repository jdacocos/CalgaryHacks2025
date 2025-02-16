import pygame

pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer with Gravity Switch Block")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)        # Player 1
GREEN = (0, 255, 0)      # Player 2
BLUE = (0, 0, 255)       # Platforms
PURPLE = (128, 0, 128)   # Kill Block
YELLOW = (255, 255, 0)   # Gravity Switch Block

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
GRAVITY = 1
JUMP_STRENGTH = -15
VELOCITY = 5

# Player placeholders
player1 = pygame.Rect(200, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
player2 = pygame.Rect(200, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
player1_vel_y = 0
player2_vel_y = 0
player1_gravity = GRAVITY
player2_gravity = GRAVITY

# Platforms (Roof, Middle, Bottom)
platforms = [
    pygame.Rect(0, 50, 800, 20),   # Roof
    pygame.Rect(0, 300, 800, 20),  # Middle
    pygame.Rect(0, 550, 800, 20)   # Bottom
]

# Kill Block (Ends the game if touched)
kill_block = pygame.Rect(350, 500, 100, 20)  

# Gravity Switch Block (Switches the gravity of the *other* player)
gravity_switch_block = pygame.Rect(600, 250, 50, 50)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # --- Player 1 Controls ---
    if keys[pygame.K_a]:  
        player1.x -= VELOCITY
    if keys[pygame.K_d]:  
        player1.x += VELOCITY
    if keys[pygame.K_w] and player1_vel_y == 0:  # Jump only when standing on a platform
        player1_vel_y = JUMP_STRENGTH * (-1 if player1_gravity < 0 else 1)

    # --- Player 2 Controls ---
    if keys[pygame.K_LEFT]:  
        player2.x -= VELOCITY
    if keys[pygame.K_RIGHT]:  
        player2.x += VELOCITY
    if keys[pygame.K_UP] and player2_vel_y == 0:  # Jump
        player2_vel_y = JUMP_STRENGTH * (-1 if player2_gravity < 0 else 1)

    # Apply gravity
    player1_vel_y += player1_gravity
    player1.y += player1_vel_y
    player2_vel_y += player2_gravity
    player2.y += player2_vel_y

    # --- Collision Detection ---
    for platform in platforms:
        # Player 1 collision
        if player1.colliderect(platform) and player1_vel_y > 0:
            player1.y = platform.y - PLAYER_HEIGHT
            player1_vel_y = 0  # Stop falling

        # Player 2 collision
        if player2.colliderect(platform) and player2_vel_y > 0:
            player2.y = platform.y - PLAYER_HEIGHT
            player2_vel_y = 0  # Stop falling

    # Prevent players from falling off the screen
    if player1.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
        player1.y = SCREEN_HEIGHT - PLAYER_HEIGHT
        player1_vel_y = 0

    if player2.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
        player2.y = SCREEN_HEIGHT - PLAYER_HEIGHT
        player2_vel_y = 0

    # --- Kill Block Collision ---
    if player1.colliderect(kill_block) or player2.colliderect(kill_block):
        print("Game Over! A player touched the Kill Block.")
        running = False  # Ends the game

    # --- Gravity Switch Block Collision ---
    if player1.colliderect(gravity_switch_block):  
        player2_gravity *= -1  # Switch Player 2's gravity
        print("Player 1 hit the Gravity Switch! Player 2's gravity is now:", player2_gravity)

    if player2.colliderect(gravity_switch_block):  
        player1_gravity *= -1  # Switch Player 1's gravity
        print("Player 2 hit the Gravity Switch! Player 1's gravity is now:", player1_gravity)

    # --- Draw Everything ---
    screen.fill(BLACK)  # Clear screen

    # Draw Player 1
    pygame.draw.rect(screen, RED, player1)

    # Draw Player 2
    pygame.draw.rect(screen, GREEN, player2)

    # Draw Platforms
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)

    # Draw Kill Block
    pygame.draw.rect(screen, PURPLE, kill_block)

    # Draw Gravity Switch Block
    pygame.draw.rect(screen, YELLOW, gravity_switch_block)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
