import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()  # Correct call to the superclass initializer
        self.image = pygame.Surface((4, 15))
        self.image.fill((255, 0, 0))  # This line creates a small rectangular image to represent our laser
        # in the game, where the width is 4 pixels, and the height is 15 pixels.
        self.rect = self.image.get_rect(center=position)
        # Use the center point to position it. To position the laser, we can achieve this by
        # providing specific coordinates as an argument to the class.
        # These coordinates determine where the laser will appear on the screen when it's first created.