import pygame
from pygame.locals import *
import random


pygame.init()

color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

ALTURA = 600
ANCHURA = 720
SPEED = 30

FPS = 10

FramePerSeC = pygame.time.Clock()

object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))




CREARVENTANA = pygame.display.set_mode((ANCHURA, ALTURA))
pygame.display.set_caption("TETRIS")

def generarPieza():
    numrand = random.randint(1,7)
    cuadradoposx = 330
    cuadradoposy = 30
    if numrand == 1: #Cuadrado
        pieza = [[cuadradoposx, cuadradoposy],[cuadradoposx + 30, cuadradoposy],
            [cuadradoposx, cuadradoposy + 30],[cuadradoposx + 30, cuadradoposy + 30]]
        
    elif numrand == 2: #palo
        pieza = [[cuadradoposx, cuadradoposy],[cuadradoposx, cuadradoposy + 30],
            [cuadradoposx, cuadradoposy + 60],[cuadradoposx, cuadradoposy + 90]]
    elif numrand == 3: # la S
        pieza = [[cuadradoposx + 30, cuadradoposy],[cuadradoposx + 60, cuadradoposy],
            [cuadradoposx, cuadradoposy + 30],[cuadradoposx + 30, cuadradoposy + 30]]
    elif numrand == 4: # la Z
        pieza = [[cuadradoposx, cuadradoposy],[cuadradoposx + 30, cuadradoposy],
            [cuadradoposx + 30, cuadradoposy + 30],[cuadradoposx + 60, cuadradoposy + 30]]
    elif numrand == 5: # la J
        pieza = [[cuadradoposx, cuadradoposy],[cuadradoposx , cuadradoposy + 30],
            [cuadradoposx, cuadradoposy + 60],[cuadradoposx - 30, cuadradoposy + 60]]
    elif numrand == 6: # la L
        pieza = [[cuadradoposx, cuadradoposy],[cuadradoposx, cuadradoposy + 30],
            [cuadradoposx, cuadradoposy + 60],[cuadradoposx + 30, cuadradoposy + 60]]
    else: # la T
        pieza = [[cuadradoposx, cuadradoposy],[cuadradoposx - 30, cuadradoposy + 30],
            [cuadradoposx, cuadradoposy + 30],[cuadradoposx + 30, cuadradoposy + 30]]
        
    return pieza

class Pieza(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        tampieza = generarPieza()
        #pieza1
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(color4)
        self.rect = self.surf.get_rect()
        self.rect.center = (tampieza[0][0], tampieza[0][1])
        #pieza2
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(color4)
        self.rect = self.surf.get_rect()
        self.rect.center = (tampieza[1][0], tampieza[1][1])
        #pieza3
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(color4)
        self.rect = self.surf.get_rect()
        self.rect.center = (tampieza[2][0], tampieza[2][1])
        #pieza4
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(color4)
        self.rect = self.surf.get_rect()
        self.rect.center = (tampieza[3][0], tampieza[3][1])
    
    
    def move(self):
        if (self.rect.bottom < 570):
            self.rect.move_ip(0,SPEED)
            
        
        
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 75:
          if pressed_keys[K_LEFT]:
              self.rect.move_ip(-30, 0)
        if self.rect.right < 375:       
          if pressed_keys[K_RIGHT]:
              self.rect.move_ip(30, 0)
        
    
    def draw(self, surface):
        surface.blit(self.surf, self.rect)
    
    
Pieza1 = Pieza()

Contador = 0
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        print(event)
    Pieza1.update()
    if Contador %60 == 0:
        Pieza1.move()
    
    Contador += 5
    
    CREARVENTANA.fill((0,0,0))
    Pieza1.draw(CREARVENTANA)
    
    pygame.display.update()
    FramePerSeC.tick(FPS)
    
    
    
    
    
    
    
    
    
