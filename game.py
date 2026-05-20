import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen info
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Cream Scoop Scoop!")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("new_red.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #?
        
    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0) #?
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cone.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (150, 150))
        #self.rect.center = (160, 520)
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-15, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(15, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
    
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    
    pygame.display.update()
    FramePerSec.tick(FPS)