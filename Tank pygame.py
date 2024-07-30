import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Tankzzzz')
clock = pygame.time.Clock()

ground_surface = pygame.image.load('Graphics/ground1.png').convert()
sky_surface = pygame.image.load('Graphics/Sky (3) copy.png').convert()

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

    lasers_group.draw(screen)  # Draw all lasers in the group
    lasers_group.update()  # Update all lasers in the group (if any update logic is added later)
   


    tank_group.update()
    tank_group.draw(screen)


    pygame.display.update()
    clock.tick(60)
    













