# import
import pygame, sys
from pygame.locals import *
import random, time

# init
pygame.init()

# fps
FPS = 60
clock = pygame.time.Clock()

# colors
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen info
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED = 5
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(GREY)
pygame.display.set_caption("Scoop it up!")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("new_red.png")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(75, SCREEN_WIDTH - 75), 100)
        
    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(75, SCREEN_WIDTH - 75), 100)
    
    #def draw(self, surface):
    #    surface.blit(self.image, self.rect)
        
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cone.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)
    
    #def draw(self, surface):
    #    surface.blit(self.image, self.rect)
    
# sprites
P1 = Player()
E1 = Enemy()

# sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

# new user event? speed

# loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #P1.update()
    #E1.move()
    
    DISPLAYSURF.fill(GREY)
    # move and draw sprites
    for sprite in all_sprites:
        DISPLAYSURF.blit(sprite.image, sprite.rect)
        sprite.move()
        
    # collisions
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        pygame.display.update()
        for sprite in all_sprites:
            sprite.kill()
        time.sleep(2) # ?
        pygame.quit()
        sys.exit()
    
    #P1.draw(DISPLAYSURF)
    #E1.draw(DISPLAYSURF)
    
    pygame.display.update()
    clock.tick(FPS)