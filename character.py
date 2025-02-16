import pygame

class Character:
    def __init__(self, x, y, image_paths, controls, screen_width):
        self.speed = 10
        self.controls = controls
        self.width = 50
        self.height = 50
        self.facing_right = True
        self.y = y
        self.x = x
        self.screen_width = screen_width
        self.reset_screen = False

        # Load character images
        self.images = {
            "idle": pygame.transform.scale(pygame.image.load(image_paths["idle"]), (50, 50)),
            "walk": pygame.transform.scale(pygame.image.load(image_paths["walk"]), (50, 50)),
            "jump": pygame.transform.scale(pygame.image.load(image_paths["jump"]), (50, 50))
        }
        self.current_image = self.images["idle"]

        # Get rectangle for positioning and collision
        self.rect = self.current_image.get_rect()
        self.rect.topleft = (x, y)

        # Physics
        self.GRAVITY = 1
        self.JUMP_STRENGTH = -15
        self.y_velocity = 0
        self.on_ground = False
        self.ground_y = y

        self.moving_left = False
        self.moving_right = False
        self.is_jumping = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls["left"]:
                self.moving_left = True
                self.facing_right = False
            if event.key == self.controls["right"]:
                self.moving_right = True
                self.facing_right = True
            if event.key == self.controls["up"] and self.on_ground:
                self.y_velocity = self.JUMP_STRENGTH
                self.on_ground = False
                self.is_jumping = True  # Start jumping
                self.current_image = self.images["jump"]  # Show jump image immediately

        elif event.type == pygame.KEYUP:
            if event.key == self.controls["left"]:
                self.moving_left = False
            if event.key == self.controls["right"]:
                self.moving_right = False

    def move(self):

        # Apply gravity
        self.y_velocity += self.GRAVITY
        self.y += self.y_velocity

        # Define wrapping boundaries
        left_boundary = 150 - self.width
        right_boundary = 1050

        # Check if character lands on ground
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.y_velocity = 0
            self.on_ground = True
            self.is_jumping = False

        if self.is_jumping:
            self.current_image = self.images["jump"]
        elif self.moving_left or self.moving_right:
            self.current_image = self.images["walk"]
        else:
            self.current_image = self.images["idle"]

        if self.moving_left:
            self.x -= self.speed

        if self.moving_right:
            self.x += self.speed

        #Wrapping:
        if self.x < left_boundary:
            self.x = right_boundary
            self.reset_screen = True
        elif self.x > right_boundary:
            self.x = left_boundary
            self.reset_screen = True

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        image_to_draw = self.current_image
        if not self.facing_right:
            image_to_draw = pygame.transform.flip(self.current_image, True, False)  # Flip horizontally

        screen.blit(image_to_draw, self.rect)

    #CALL THIS TO RETURN ROOM STATUS. IT WILL RETURN TRUE IF It has changed room.
    def get_level_status (self):
        return self.reset_screen
    
    #CALL THIS TO RESET ROOM STATUS, RIGHT AFTER DOING SO.
    def reset_screen (self):
        self.reset_screen = False
