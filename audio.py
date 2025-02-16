import pygame

pygame.mixer.init()


# Player 1
jump_player1 = pygame.mixer.Sound("assets/audio/jump_up.mp3")
death_player1 = pygame.mixer.Sound("assets/audio/death_up.mp3")
victory_player1 = pygame.mixer.Sound("assets/audio/victory_up.mp3")

# Player 2
jump_player2 = pygame.mixer.Sound("assets/audio/jump_down.mp3")
death_player2 = pygame.mixer.Sound("assets/audio/death_down.mp3")
victory_player2 = pygame.mixer.Sound("assets/audio/victory_down.mp3")

# Background Music
def play_background_music():
    pygame.mixer.music.load("assets/audio/background_music.mp3")
    pygame.mixer.music.play(-1)  # Loop music

def stop_background_music():
    pygame.mixer.music.stop()

def play_sound(effect): # insert soundeffect as parameter
    effect.play()
