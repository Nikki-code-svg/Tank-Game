import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position,speed, screen_height):
        super().__init__()  # Correct call to the superclass initializer
        self.image = pygame.Surface((4, 15))
        self.image.fill((255, 0, 0))  # This line creates a small rectangular image to represent our laser
        # in the game, where the width is 4 pixels, and the height is 15 pixels.
        self.rect = self.image.get_rect(center=position)
        # Use the center point to position it. To position the laser, we can achieve this by
        # providing specific coordinates as an argument to the class.
        # These coordinates determine where the laser will appear on the screen when it's first created.
        self.speed = speed
        self.screen_height = screen_height 

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height + 15 or self.rect.y <0:
            self.kill()
    # to move a laser you just have to reposition its rectangle. Since
    # can move only in the y direction we just have to add or remove some pixels
    # to move it up or down. The number of pixels to move per frame will be a class argument 
    # named speed 
    # if we want to move the laser up, we will provide a positive value to 
    # the speed argument. If we want to move the laser down we will provide a negative one
