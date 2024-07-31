import pygame
from sys import exit
import random
from pygame import mixer
from lib.high_score_manager import Highscore

pygame.init()
screen = pygame.display.set_mode((1000, 800))
screen_rect = screen.get_rect()  # part of tank can't leave screen
pygame.display.set_caption('Tankzzzz')
clock = pygame.time.Clock()

##Font##
title_font = pygame.font.Font("font/tank.ttf", 40) #get font
title_surface = title_font.render("Tankzzz", False, "Purple")
title_rect = title_surface.get_rect(center = (500, 400))

high_score_surface = title_font.render("High Scores", False, "Purple")
high_score_rect = high_score_surface.get_rect(center = (500, 50))


# Load surfaces
ground_surface = pygame.image.load('Graphics/ground1.png').convert()
sky_surface = pygame.image.load('Graphics/Sky (3) copy.png').convert()

alien_images = [
    'Graphics/Ship6/Ship6.png',
    'Graphics/Ship5/Ship5.png',
    'Graphics/Ship3/Ship3.png'
]

####Score Board####
def display_high_score(score_font, user, score, disp):
    score_surface = score_font.render(f"{user}.......{score}", False, "White")
    score_rect = score_surface.get_rect(center = (500, disp))
    screen.blit(score_surface, score_rect)



####states/screens
#Start page
high_scores = False
game_active = False
#game_over/enter initials

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0):
        super().__init__()
        image_path = random.choice(alien_images)
        original_alien_img = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotate(original_alien_img, angle)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = random.randint(1, 3)

    def update(self):
        self.rect.y += self.velocity
        if self.rect.top >= screen.get_height():
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, screen.get_width() - self.rect.width)

alien_group = pygame.sprite.Group()

rotation_angle = 270
for i in range(5):
    alien = Aliens(i * 150, -50, rotation_angle)
    alien_group.add(alien)

mixer.init()
background_music = mixer.music.load('sounds/mixkit-game-level-music-689.wav')
mixer.music.play()

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height, offset_x=-24, offset_y=-95):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill((255, 0, 0))
        adjusted_pos = (pos[0] + offset_x, pos[1] + offset_y)
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
        original_image = pygame.image.load('Graphics/green.png').convert_alpha()
        self.image = pygame.transform.scale(original_image, (300, 196))
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_active and not high_scores:
                        high_scores = True
                elif high_scores and not game_active:
                        high_scores = False
                        game_active = True


    if game_active:
        tank.rect.clamp_ip(screen_rect) 

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 600))

        alien_group.update()
        alien_group.draw(screen)

        tank_group.update()
        tank_group.draw(screen)
        
        tank.lasers_group.draw(screen)
    
    elif high_scores:
        screen.fill("Grey")
        screen.blit(high_score_surface, high_score_rect)

        display = 200
        for i in range(0,5):
            display_high_score(title_font, Highscore.get_high_scores()[i][0], Highscore.get_high_scores()[i][1], display)
            display+=100
    
    elif not game_active and not high_scores:
        screen.fill("Grey")
        screen.blit(title_surface, title_rect)

    pygame.display.update()
    clock.tick(60)


####Scoring/collision Logic:
# #alien
# alien_rect.y += speed ##speed at which moving down
# if bad_guy_rect collide with bullet 
#     bad_guy_rect.bottom = -300 #reset to top
#     bad_guy_rect.bottom = random.randint(x,y)
#     ##Set a floor and ceiling for my speed, 5 and 12
    
#     speed =random.randrange(5,12)
#     score +=1