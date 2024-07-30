import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1000, 800))
screen_rect = screen.get_rect() # part of tank cant leave screen
pygame.display.set_caption('Tankzzzz')
clock = pygame.time.Clock()

# Load surfaces
ground_surface = pygame.image.load('Graphics/ground1.png').convert()
sky_surface = pygame.image.load('Graphics/Sky (3) copy.png').convert()

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height, offset_x=-24, offset_y=-95):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill((255, 0, 0))
        adjusted_pos = (pos[0] + offset_x, pos[1]+ offset_y)
        self.rect = self.image.get_rect(center=adjusted_pos)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
         resized_tank
        # put all images here for different movements/ put self on everything in the init
        #Define our image
        original_image = pygame.image.load('Graphics/green.png').convert_alpha()
        self.image = pygame.transform.scale(original_image, (300,196))
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

    def collision(self):
        # collide_rect(left, right)
        pass
       
#tank instance
tank = Tank(100, 500)
tank_group = pygame.sprite.Group()
tank_group.add(tank)

# laser = Laser((100, 100))
# laser2 = Laser((100, 200))  

lasers_group = pygame.sprite.Group()
# Create a group that will hold all the laser beams that the spaceship will fire
# lasers_group.add(laser, laser2)

        
        self.rect = self.image.get_rect(topleft=(x, y))
        self.lasers_group = pygame.sprite.Group()
        self.screen_height = pygame.display.get_surface().get_height()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.shoot_laser()

    def shoot_laser(self):
        self.laser_ready = False
        laser = Laser(self.rect.center, 5, self.screen_height)
        self.lasers_group.add(laser)
        self.laser_time = pygame.time.get_ticks()

    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def update(self):
        self.move()
        self.lasers_group.update()
        self.recharge_laser()

# Initialize tank
tank = Tank(100, 600)
tank_group = pygame.sprite.GroupSingle(tank)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    resized_tank
    tank.rect.clamp_ip(screen_rect) # tank can't leave screen
    tank.move()
     

=======
    # Update and draw the scene

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 600))

    tank_group.update()
    tank_group.draw(screen)
    tank.lasers_group.draw(screen)

    pygame.display.update()
    clock.tick(60)