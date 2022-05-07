from utils.Tableros import Levels
import pygame

pygame.font.init()
# tamano de la ventana
ventana = pygame.display.set_mode((500, 585))
pygame.display.set_caption("SUDOKU") 
x = 0
y = 0
cuadros = 500 / 9
val = 0
#Tablero
lvl = Levels.generateLevel()

grid =[
        lvl[0],
        lvl[1],
        lvl[2],
        lvl[3],
        lvl[4],
        lvl[5],
        lvl[6],
        lvl[7],
        lvl[8], 
    ]
 
# font para el texto de las intrucciones y numeros
ftexto1 = pygame.font.SysFont("arial", 40)
ftexto2 = pygame.font.SysFont("arial", 20)
#crear cordenadas para colocar el cursor o valores
def cordenadas(pos):
    global x
    x = pos[0]//cuadros
    global y
    y = pos[1]//cuadros
 
def dibujar_cursor():
    for i in range(2):
        pygame.draw.line(ventana, (255, 0, 0), (x * cuadros-3, (y + i)*cuadros), (x * cuadros + cuadros + 3, (y + i)*cuadros), 7)
        pygame.draw.line(ventana, (255, 0, 0), ( (x + i)* cuadros, y * cuadros ), ((x + i) * cuadros, y * cuadros + cuadros), 7)  
       
def dibujar_lineas():
    #crear numeros dentro del tablero
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
                # color de los numeros
                text = ftexto1.render(str(grid[i][j]), 1, (0, 0, 0))
                ventana.blit(text, (i * cuadros + 15, j * cuadros + 0))
    # crear lineas         
    for i in range(10):
        if i % 3 == 0 :
            lin = 7
        else:
            lin = 1
        #color lineas horizontales
        pygame.draw.line(ventana, (101, 198, 187), (0, i * cuadros), (500, i * cuadros), lin)
        #color lineas verticales
        pygame.draw.line(ventana, (13, 180, 185), (i * cuadros, 0), (i * cuadros, 500), lin)     
     
def valalores_Tab(val):
    text = ftexto1.render(str(val), 1, (255, 0, 0))
    ventana.blit(text, (x * cuadros + 15, y * cuadros + 15))   
 #validar valores y evitar su repeticion en dicha posiciones
def valid(p, i, j, val):
    for fila in range(9):
        if p[i][fila]== val:
            return False
        if p[fila][j]== val:
            return False
    fila = i//3
    columna = j//3
    for i in range(fila * 3, fila * 3 + 3):
        for j in range (columna * 3, columna * 3 + 3):
            if p[i][j]== val:
                return False
    return True
# resolver sudoku boton
def solve(grid, i, j):
     
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    for fila in range(1, 10):
        if valid(grid, i, j, fila)== True:
            grid[i][j]= fila
            global x, y
            x = i
            y = j
            # color principal del fondo del tablero
            ventana.fill((255, 255, 255))
            dibujar_lineas()
            dibujar_cursor()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            # color del fondo del recorido automatico(boton resolver)
            ventana.fill((255, 255, 255))
         
            dibujar_lineas()
            dibujar_cursor()
            pygame.display.update()
            pygame.time.delay(1)  
    return False 
 
def instrucciones():
    text = ftexto2.render("F para Llenar / R para Resetear", 1, (0, 0, 0))
    text2 = ftexto2.render("Presiona Enter para resolver", 1, (0, 0, 0))
    ventana.blit(text, (20, 520))       
    ventana.blit(text2, (20, 540))
 
run = True
bandera = 0
bandera2 = 0
e = 0
error = 0
while run:
    # color de fondo
    ventana.fill((255, 255, 255))
    # Recorra los eventos almacenados en event.get()
    for accion in pygame.event.get():
        # salir del juego
        if accion.type == pygame.QUIT:
            run = False 
        # tomar la posicion del mouse y los numeros   
        if accion.type == pygame.MOUSEBUTTONDOWN:
            bandera = 1
            pos = pygame.mouse.get_pos()
            cordenadas(pos)
        # tomar o leer las teclas que uno presione a base de un IF   
        if accion.type == pygame.KEYDOWN:
            if accion.key == pygame.K_LEFT:
                x-= 1
                bandera = 1
            if accion.key == pygame.K_RIGHT:
                x+= 1
                bandera = 1
            if accion.key == pygame.K_UP:
                y-= 1
                bandera = 1
            if accion.key == pygame.K_DOWN:
                y+= 1
                bandera = 1   
            if accion.key == pygame.K_1:
                val = 1
            if accion.key == pygame.K_2:
                val = 2   
            if accion.key == pygame.K_3:
                val = 3
            if accion.key == pygame.K_4:
                val = 4
            if accion.key == pygame.K_5:
                val = 5
            if accion.key == pygame.K_6:
                val = 6
            if accion.key == pygame.K_7:
                val = 7
            if accion.key == pygame.K_8:
                val = 8
            if accion.key == pygame.K_9:
                val = 9 
            if accion.key == pygame.K_RETURN:
                bandera2 = 1  
            # Crear la accion R para reiniciar o limpiar tablero
            if accion.key == pygame.K_r:
                e = 0
                error = 0
                bandera2 = 0
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # crear la accion F para llamar un tablero o nivel
            if accion.key == pygame.K_f:
                e = 0
                error = 0
                bandera2 = 0
                lvl = Levels.generateLevel()

                grid =[
                        lvl[0],
                        lvl[1],
                        lvl[2],
                        lvl[3],
                        lvl[4],
                        lvl[5],
                        lvl[6],
                        lvl[7],
                        lvl[8], 
                    ]
    if bandera2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            e = 1
        bandera2 = 0   
    if val != 0:           
        valalores_Tab(val)
        if valid(grid, int(x), int(y), val)== True:
            grid[int(x)][int(y)]= val
            bandera = 0
        else:
            grid[int(x)][int(y)]= 0 
        val = 0   
    
    if bandera == 1:
        dibujar_cursor()      
    instrucciones()   
    dibujar_lineas()
    # Update ventana
    pygame.display.update() 
#cerra juego o ventana   
pygame.quit() 