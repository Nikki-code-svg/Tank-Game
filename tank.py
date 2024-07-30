import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # put all images here for different movements/ put self on everything in the init
        #Define our image
        self.image = pygame.image.load('Graphics/pixil-frame-0.png').convert_alpha()
        # Get rect
        self.rect = self.image.get_rect()
        #Position the image
        self.rect.topleft = (x,y)
        # self.gravity = 0


    def move(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_RIGHT] and self.rect.bottom >= 600:
           self.rect.x = 10
       else: 
           keys[pygame.K_LEFT] and self.rect.bottom >= 600;
           self.rect.x = -10
        
           
    
    # def apply_gravity(self):
    #     self.gravity += 1
    #     # so our player does not fall outside of the screen
    #     self.rect.y = self.gravity
    #     if self.rect.bottom >= 600:
    #         self.rect.bottom = 600

    #if we have animation with a different image
    # def animation_state(self):
    #     if self.rect.bottom < 300:
    #         self.image = self.tank_gun
    #     else:
    #         self.tank_index += 0.1
    #         if self.tank_index >= len(self.tank_shoot):tank_index = 0
    #         self.image = self.tank_shoot[int(tank_index)]

    
    def update(self):
        self.move()
        # self.apply_gravity()
        self.check_collision()
        # self.animation_state()

    def check_collision(self):
       
       pass

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'alien':
           alien_1 = pygame.image.load('').convert_alpha()
           self.frames = [alien_1]
           y_pos = 210
           
        else: 
            enemy_1 = pygame.image.load('').convert_alpha()
            self.frames = [enemy_1]
            y_pos = 300

        self.animation_index = 0

        # self.image = self.frames[self.animation_index]
        # self.rect = self.image.get_rect(midbottom = (random.randint(900, 1100), y_pos))


#create tank group
tank_group = pygame.sprite.Group()
#create and position tank
tank = Tank(0, 600)


# to call the function need the update function
# put character on screen draw()
tank_group.update()
tank_group.draw(screen)