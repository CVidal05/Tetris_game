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
Velbajada = 50
Vpos = pygame.Vector2(COLUMNAS // 2 , -3)
Reloj = 15


# Colores 
Negro = (30, 30, 30)
Gris = (60, 60, 60)
Blanco = (200, 200, 200)
Rojo = (255,0,0)
Azul = (0,0,255)
Amarillo = (255,255,0)
Cyan = (0,255,255)
Lima = (0,225,0)
Naranja = (255,152,0)
Morado = (138,43,226)

#Listas de piezas
T = [[(0,0),(-1,0),(1,0),(0,-1)],Morado]
L = [[(0,0),(0,-1),(1,0),(1,1)],Naranja]
J = [[(0,0),(0,-1),(0,1),(-1,1)],Azul]
S = [[(0,0),(-1,0),(0,-1),(1,-1)],Lima]
Z = [[(0,0),(1,0),(0,-1),(-1,-1)],Rojo]
O = [[(0,0),(0,-1),(1,0),(1,-1)],Amarillo]
I = [[(0,0),(0,-1),(0,-2),(0,1)],Cyan]
piezas = [T,L,J,S,Z,O,I]

Contador = 0

# Clase de la ventana del juego , se crea una display para poner lo que queramos sobre ella y esa display ponerla sobre la display_surface que es la pantalla principal
class Game:
    def __init__(self):
        
        # General
        self.surface = pygame.Surface((LongJuego,AltJuego)) # Ventana
        self.display_surface = pygame.display.get_surface() # Recojo la pantalla principal
        self.rect = self.surface.get_rect(topleft = (MARGEN,MARGEN*3))
        self.grupo = pygame.sprite.Group() # Un contenedor para guardar varias clases sprite, ya que estos sprites son los cuadrados, el contenedor es la pieza
        
        # Lineas
        self.lineas_surface = self.surface.copy() # creo una ventana donde se dibujan las lineas, es igual que la self.surface
        self.lineas_surface.fill((0,255,0)) # La pinto de verde para luego quitarlo
        self.lineas_surface.set_colorkey((0,255,0))
        self.lineas_surface.set_alpha(120)
        
        # Pieza
        # Lista de piezas para colisiones
        self.matrizPiezas = []
        for fil in range(FILAS):
            self.matrizPiezas.append([])
            for col in range(COLUMNAS):
                self.matrizPiezas[fil].append(0)
        # Pieza que está en juego --- llama a la clase Pieza ( tipo, grupo de cuadrados, función para crear otra pieza, Matriz para colisiones entre piezas)
        self.pieza = Pieza(random.randint(6,6), self.grupo, self.crearNuevaPieza, self.matrizPiezas)
       
    def dibujo_lineas(self):
        for col in range(1,COLUMNAS):
            pygame.draw.line(self.lineas_surface, Blanco, (col*tamañoCeldas,0),(col*tamañoCeldas,AltJuego), 1) # (ventana, color, pos inicial, pos final, anchura)
        for fil in range(1,FILAS):
            pygame.draw.line(self.lineas_surface, Blanco, (0,fil*tamañoCeldas),(LongJuego,fil*tamañoCeldas), 1)
            
        self.surface.blit(self.lineas_surface, (0,0)) # Blit en la surface de la ventana la surfaces de las lineas
        
    def moverbajo(self):
        self.pieza.moverbajo()
        
    def input(self):
        
        # Movimientos laterales
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.pieza.moverizq()
        if teclas[pygame.K_RIGHT]:
            self.pieza.moverder()
        
        # Rotación
        if teclas[pygame.K_UP]:
            self.pieza.rotacion()
            
    
    def crearNuevaPieza(self):
        self.lineaCompleta()
        self.pieza = Pieza(random.randint(6,6), self.grupo, self.crearNuevaPieza, self.matrizPiezas)
        
    def lineaCompleta(self): # Comprueba si alguna fila está completa
        cont = 0
        borrarFil = []
        for fil in range(FILAS):
            for col in range(COLUMNAS):
                if self.matrizPiezas[fil][col] != 0:
                    cont +=1
            if cont == 10:
                borrarFil.append(fil)
            cont = 0
                    
        if borrarFil:
            for borrar in borrarFil:
                # Eliminar una línea
                for cuadradito in self.matrizPiezas[borrar]:
                    cuadradito.kill()
                # Mover abajo los bloques
                for fil in self.matrizPiezas:
                    for cuadradito in fil: # Bajamos los cuadrados que esten por encima de la linea eliminada
                        if cuadradito != 0 and cuadradito.pos.y < borrar:
                            cuadradito.pos.y += 1
                            
                # Reconstruir la matriz
                self.matrizPiezas = []
                for fil in range(FILAS):
                    self.matrizPiezas.append([])
                    for col in range(COLUMNAS):
                        self.matrizPiezas[fil].append(0)
                        for cuadradito in self.grupo:
                            if fil == cuadradito.pos.y and col == cuadradito.pos.x:
                                self.matrizPiezas[fil][col] = cuadradito

#                 for col in range(COLUMNAS):
#                     self.matrizPiezas[borrar][col] = 0

    def run(self):
        # Actualizar
        self.grupo.update()
        self.input()
        
        self.surface.fill(Gris)
        self.grupo.draw(self.surface)
        
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
class Bloque(pygame.sprite.Sprite):
    def __init__(self, grupo, pos, color):   # Características de la pieza (grupo, posición, color)
        # General
        super().__init__(grupo)
        self.image = pygame.Surface((tamañoCeldas,tamañoCeldas))
        self.image.fill(color)
        
        
        # Posición
        self.pos = pygame.Vector2(pos) + Vpos
        self.rect = self.image.get_rect(topleft = (self.pos * tamañoCeldas))
    
    def update(self):
        self.rect.topleft = self.pos * tamañoCeldas
        
    # Colisiones
    # por limite del mapa o colisión con otra pieza
    def colisionLateralIzq(self, X, matrizPieza):
        if not(0 <= X) or (int(self.pos.y) >= 0 and matrizPieza[int(self.pos.y)][X]):
            return True

    def colisionLateralDer(self, X, matrizPieza):
        if not(X < COLUMNAS) or (int(self.pos.y) >= 0 and matrizPieza[int(self.pos.y)][X]):
            return True
    def colisionInferior(self, Y, matrizPieza): 
        if not(Y < FILAS) or (Y >= 0 and matrizPieza[Y][int(self.pos.x)]): 
            return True
    
    # Colisiones
    def colisiones(self, cuadradoCentral):
        distancia = self.pos - cuadradoCentral_pos
        rotacion = distancia.rotate(90)
        nuevaPos = cuadradoCentral + rotacion

# Crea la clase Pieza, con las características de una pieza
class Pieza():
    def __init__(self, tipo, grupo, crearNuevaPieza, matrizPiezas):
        self.forma = piezas[tipo][0]
        self.color = piezas[tipo][1]
        self.crearNuevaPieza = crearNuevaPieza # va a llamar a la función de la clase GAME
        self.matrizPiezas = matrizPiezas
        # for de la pieza
        self.conjunto_pieza = [Bloque(grupo, pos, self.color) for pos in self.forma]
    
    # Colisiones
    def colisionLateralIzq(self, pieza):
        colisionesIzq = [Bloque.colisionLateralIzq(cuadradito, int(cuadradito.pos.x - 1), self.matrizPiezas) for cuadradito in self.conjunto_pieza]
        if any(colisionesIzq) == True:
            return True
        else:
            return False
    
    def colisionLateralDer(self, pieza):
        colisionesDer = [Bloque.colisionLateralDer(cuadradito, int(cuadradito.pos.x + 1), self.matrizPiezas) for cuadradito in self.conjunto_pieza]
        if any(colisionesDer) == True:
            return True
        else:
            return False
    
    def colisionInferior(self, pieza):
        colisionesInf = [Bloque.colisionInferior(cuadradito, int(cuadradito.pos.y + 1), self.matrizPiezas) for cuadradito in self.conjunto_pieza]
        if any(colisionesInf) == True:
            return True
        else:
            return False

    # Movimiento
    def moverbajo(self):
        if self.colisionInferior(self.conjunto_pieza) != True: # Si la función colisión retornase True es que hay algo debajo, y por eso en el Else para de moverse
            for cuadradito in self.conjunto_pieza:
                cuadradito.pos.y += 1
        else: # Llega al suela y se ejecuta la función para crear la nueva pieza
            for cuadradito in self.conjunto_pieza:  # En la pos de cada cuadrado de una pieza dentro de la matriz guardo ese mismo cuadrado
                self.matrizPiezas[int(cuadradito.pos.y)][int(cuadradito.pos.x)] = cuadradito
            self.crearNuevaPieza()

    def moverizq(self):
        if self.colisionLateralIzq(self.conjunto_pieza) != True:
            for cuadradito in self.conjunto_pieza:
                cuadradito.pos.x -= 1
    def moverder(self):
        if self.colisionLateralDer(self.conjunto_pieza) != True:
            for cuadradito in self.conjunto_pieza:
                cuadradito.pos.x += 1
    # Rotación
    def rotacion(self):
        if self.tipo != 5: # Si la pieza no es un cuadrado
            cuadradoCentral = self.conjunto_pieza[0].pos
            nuevosBloques = []
            for cuadradito in self.pieza:
                Bloque.rotacion(cuadradoCentral)
    
# Comienzo de Ejecución
juego = True
#general 
pygame.init()
display_surface = pygame.display.set_mode((LongVentana,AltVentana)) # Tamaño de la pantalla
clock = pygame.time.Clock()
pygame.display.set_caption('TETRIS')
        
# Componentes
game = Game() # se le atribuye la clase, ventana de juego
score = Score() # ventan del Score
titulo = Titulo()
        
        


# Loop del juego
while juego==True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Velbajada2 = 1
        else:
            Velbajada2 = Velbajada
            
       
    # display
    display_surface.fill(Negro)
            
    # componentes
    game.run() # llama a la función run de la variable game
    score.run()
    titulo.run()
    #Juego
    
    if Contador % Velbajada2 == 0:
        game.moverbajo()
            
            
    # Actualización del juego
    Contador = Contador + 5
            
    pygame.display.update()
    clock.tick(Reloj)



