import pygame
import numpy as np


def generarCuadrado():
    pygame.draw.rect(ventana, (255,0,255), (cuadradoposx, cuadradoposy, tamanyos,tamanyos))
    
def moverCuadrado(cuadradoposy,speed):
    while cuadradoposy <= 540:
        pygame.draw.rect(ventana, (255,0,255), (cuadradoposx, cuadradoposy, tamanyos,tamanyos))
        cuadradoposy = cuadradoposy + speed
        pygame.display.flip()
        pygame.time.Clock().tick(3)
   


tamanyos = 30
cuadradoposx = 330
cuadradoposy = 30
        
pygame.init()
ventana = pygame.display.set_mode((720,600))
pygame.display.set_caption("Ejemplo 3")
pygame.key.set_repeat(1,50)
ventana.fill((255, 255, 255))
speed = 30
jugando = True
        
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    
    pygame.draw.line(ventana, (0,255,9), (165,0), (165,600), width=30)
    pygame.draw.line(ventana, (255,255,9), (180,585), (555,585), width=30)
    pygame.draw.line(ventana, (255,255,9), (555,0), (555,600), width=30) 
    generarCuadrado()
    moverCuadrado(cuadradoposy,speed)
    
    
    
    
    pygame.display.flip()
    pygame.time.Clock().tick(3)
pygame.quit()



