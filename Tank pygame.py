import pygame
from lasers import Laser
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Tankzzzz')
clock = pygame.time.Clock()

ground_surface = pygame.image.load('Graphics/ground1.png').convert()
sky_surface = pygame.image.load('Graphics/Sky (3) copy.png').convert()

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

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 600))

    lasers_group.draw(screen)  # Draw all lasers in the group
    lasers_group.update()  # Update all lasers in the group (if any update logic is added later)

    pygame.display.update()
    clock.tick(60)














