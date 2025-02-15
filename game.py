import pygame
from character import Character

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#Character Var:
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player1 = Character(200, 300, BLUE, 5, {
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d
})

player2 = Character(500, 300, RED, 5, {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT
})

while running:
    clock.tick(60)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    i = 0
    while i < 100:
        screen.fill("white")
        screen.fill("black")
        i = i+1

    #Movement
    keys = pygame.key.get_pressed()
    player1.move(keys)
    player2.move(keys)

    player1.draw(screen)
    player2.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    pygame.display.update()

pygame.quit()
