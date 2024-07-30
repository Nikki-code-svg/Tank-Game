# import pygame
# import random



# # alien = Aliens()

# class Aliens(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         #Define our image
#         self.image = pygame.image.load('Graphics/Ship6/Ship6.png').convert_alpha()
#         # Get rect
#         self.rect = self.image.get_rect(midbottom = (200,300))  
#         #Position the image
#         self.rect.topleft = (x,y)
#         #move the image
#         self.velocity = random.randint(1, 5)


#     def update(self):
#         self.rect.x += self.velocity

# alien_group = pygame.sprite.Group()


# for i in range(5):
#     alien = Aliens(i*150, 10)
#     alien_group.add(alien)


# Draw Alien sprite
# alien_group.draw(screen)