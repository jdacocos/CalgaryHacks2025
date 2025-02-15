import pygame

class Character:
    def __init__(self, x, y, color, speed, controls):
        self.x = x
        self.y = y
        self.speed = 20
        self.controls = controls
        self.color = color
        self.width = 50
        self.height = 50

    def move(self, keys):
        if keys[self.controls["up"]]:  # Move up
            self.y -= self.speed
        if keys[self.controls["down"]]:  # Move down
            self.y += self.speed
        if keys[self.controls["left"]]:  # Move left
            self.x -= self.speed
        if keys[self.controls["right"]]:  # Move right
            self.x += self.speed

    def draw(self, screen):
        """Draws the character"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
