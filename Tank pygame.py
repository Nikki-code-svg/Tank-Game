import pygame
from sys import exit
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Tankzzzz')
clock = pygame.time.Clock()

ground_surface = pygame.image.load('Graphics/ground1.png').convert()
sky_surface = pygame.image.load('Graphics/Sky (3) copy.png').convert()

alien_images = [
    'Graphics/Ship6/Ship6.png',
    'Graphics/Ship5/Ship5.png',
    'Graphics/Ship3/Ship3.png'
]

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0):
        super().__init__()
        #Randomly choose alien image
        image_path = random.choice(alien_images)
        #Define our image
        original_alien_img = pygame.image.load(image_path).convert_alpha()
        #Rotate Image
        self.image = pygame.transform.rotate(original_alien_img, angle)
        # Get rect
        self.rect = self.image.get_rect(topleft=(x,y))
        #move the image
        self.velocity = random.randint(1, 3)


    def update(self):
        self.rect.y += self.velocity
    
        if self.rect.top >= screen.get_height():
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, screen.get_width() - self.rect.width)

alien_group = pygame.sprite.Group()

rotation_angle = 270
for i in range(5):
    alien = Aliens(i*150, -50, rotation_angle)
    alien_group.add(alien)


mixer.init()
background_music = mixer.music.load('sounds/mixkit-game-level-music-689.wav')
mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 600))

    alien_group.update()
    alien_group.draw(screen)

    pygame.display.update()
    clock.tick(60)














