import pygame
import random


# Tamaño del juego
COLUMNAS = 10
FILAS = 20
tamañoCeldas = 40
LongJuego, AltJuego = (COLUMNAS * tamañoCeldas), (FILAS * tamañoCeldas)+1

# Ventana
MARGEN = 40
LongVentana = LongJuego + MARGEN * 2
AltVentana = AltJuego + MARGEN * 4

# Título
MARGENT = 5
LongTitulo = LongJuego/2 - MARGENT
AltTitulo = MARGEN*2

# Score
LongScore = LongTitulo
AltScore = MARGEN*2

# Titulo
# letra = pygame.font.SysFont('Arial', 30)
# imagTitulo = letra.render('TETRIS', True, (200,200,200), Gris )
# rectImagTitulo = imagTitulo.get_rect()

# Ajustes del juego

# Colores 
Negro = (30, 30, 30)
Gris = (60, 60, 60)
Blanco = (200, 200, 200)
Rojo = (255,0,0)
Azul = (0,0,255)

# Clase de la ventana del juego , se crea una display para poner lo que queramos sobre ella y esa display ponerla sobre la display_surface que es la pantalla principal
class Game:
    def __init__(self):
        
        # General
        self.surface = pygame.Surface((LongJuego,AltJuego)) # Ventana
        self.display_surface = pygame.display.get_surface() # Recojo la pantalla principal
        self.rect = self.surface.get_rect(topleft = (MARGEN,MARGEN*3))
        self.pieza = pygame.sprite.Group() # Un contenedor para guardar varias clases sprite, ya que estos sprites son los cuadrados, el contenedor es la pieza
        
        # Lineas
        self.lineas_surface = self.surface.copy() # creo una ventana donde se dibujan las lineas, es igual que la self.surface
        self.lineas_surface.fill((0,255,0)) # La pinto de verde para luego quitarlo
        self.lineas_surface.set_colorkey((0,255,0))
        self.lineas_surface.set_alpha(120)
        
        # Piezas
        # Linea
#        if piezaAleatoria == 1:
        self.block1 = Block(self.pieza, (3,0), Rojo)
        self.block2 = Block(self.pieza, (4,0), Rojo)
        self.block3 = Block(self.pieza, (5,0), Rojo)
        self.block4 = Block(self.pieza, (6,0), Rojo)
        
        # T inversa
#         else:
#             self.block1 = Block(self.pieza, (3,0), Azul)
#             self.block2 = Block(self.pieza, (4,0), Azul)
#             self.block3 = Block(self.pieza, (5,0), Azul)
#             self.block4 = Block(self.pieza, (4,1), Azul)
    
    def dibujo_lineas(self):
        for col in range(1,COLUMNAS):
            pygame.draw.line(self.lineas_surface, Blanco, (col*tamañoCeldas,0),(col*tamañoCeldas,AltJuego), 1) # (ventana, color, pos inicial, pos final, anchura)
        for fil in range(1,FILAS):
            pygame.draw.line(self.lineas_surface, Blanco, (0,fil*tamañoCeldas),(LongJuego,fil*tamañoCeldas), 1)
            
        self.surface.blit(self.lineas_surface, (0,0)) # Blit en la surface de la ventana la surfaces de las lineas
    
    def run(self):
        self.surface.fill(Gris)
        self.pieza.draw(self.surface)
        
        self.dibujo_lineas()
        self.display_surface.blit(self.surface, (MARGEN,MARGEN*3)) # Pone (X,Y) la ventana X en la posición Y de la pantalla prinicipal
        pygame.draw.rect(self.display_surface, Blanco, self.rect, 2, 2)# dibujo la linea exterior (ventana, color, rect, ancho, corner radio)
        
        
# Clase del Score, mismo que la ventana de juego
class Score:
    def __init__(self):
        self.surface = pygame.Surface((LongScore,AltScore)) # ventana del score
        # self.rect = self.surface.get_rect(bottom_right = (x,y)) # Crea un rectángulo del tamaño del score para luego usarlo
        self.display_surface = pygame.display.get_surface() # llamo a la ventana principal
        
    def run(self):
        self.surface.fill(Gris)
        self.display_surface.blit(self.surface, (LongJuego/2+MARGEN+MARGENT,MARGEN/2))

# Clase del título
class Titulo:
    def __init__(self):
        self.surface = pygame.Surface((LongTitulo,AltTitulo))
        self.display_surface = pygame.display.get_surface()
        
        # Letras
        
    
    def run(self):
        self.surface.fill(Gris)
        self.display_surface.blit(self.surface, (MARGEN,MARGEN/2))

# Crea un sprite, un cuadrado
class Block(pygame.sprite.Sprite):
    def __init__(self, grupo, pos, color):   # Características de la pieza (grupo, posición, color)
        # General
        super().__init__(grupo)
        self.image = pygame.Surface((tamañoCeldas,tamañoCeldas))
        self.image.fill(color)
        
        # Posición
        col,fil=pos
        x,y = col*tamañoCeldas, fil*tamañoCeldas
        self.rect = self.image.get_rect(topleft = (x,y))


# Clase del Progama de pygame
juego = True

class Main():
    def __init__(self):
        
        #general
        pygame.init()
        self.display_surface = pygame.display.set_mode((LongVentana,AltVentana)) # Tamaño de la pantalla
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('TETRIS')
        
        # Componentes
        self.game = Game() # se le atribuye la clase, ventana de juego
        self.score = Score() # ventan del Score
        self.titulo = Titulo()
    
    def run(self):
        # Loop del juego
        while juego==True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            
            # display
            self.display_surface.fill(Negro)
            
            # componentes
            self.game.run() # llama a la función run de la variable game
            self.score.run()
            self.titulo.run()
            
            # Actuslización del juego
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.run()
    
    
    
    
