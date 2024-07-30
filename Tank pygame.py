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

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # put all images here for different movements/ put self on everything in the init
        #Define our image
        img = self.image = pygame.image.load('Graphics/pixil-frame-0.png').convert_alpha()
        DFLT_IMG_SZ = (200,200)
        img = pygame.transform.scale(img, DFLT_IMG_SZ)
        # Get rect
        self.rect = self.image.get_rect()
        #Position the image
        self.rect.topleft = (x,y)
        # self.gravity = 0


    def move(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_RIGHT]:
           self.rect.x += 10
       
       if keys[pygame.K_LEFT]:
           self.rect.x -= 10


#tank instance
tank = Tank(100, 600)
tank_group = pygame.sprite.Group()
tank_group.add(tank)

laser = Laser((100, 100))
laser2 = Laser((100, 200))  

lasers_group = pygame.sprite.Group()
# Create a group that will hold all the laser beams that the spaceship will fire
lasers_group.add(laser, laser2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

   
    tank.move()


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 600))

    alien_group.update()
    alien_group.draw(screen)

    lasers_group.draw(screen)  # Draw all lasers in the group
    lasers_group.update()  # Update all lasers in the group (if any update logic is added later)
   


    tank_group.update()
    tank_group.draw(screen)


    pygame.display.update()
    clock.tick(60)
    













