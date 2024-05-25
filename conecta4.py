import sys
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

# Constantes
ANCHO = 700
ALTO = 600
COLOR_FONDO = (0, 0, 0)
COLOR_ROJO = (255, 0, 0)
COLOR_AMARILLO = (255, 255, 0)
COLOR_BLANCO = (255, 255, 255)

# Variables globales
tablero = [[0 for x in range(7)] for y in range(6)]
turno = 1
partidas_rojo = 0
partidas_amarillo = 0
partida_finalizada = False

# Funciones
def dibujar_tablero():
    for x in range(7):
        for y in range(6):
            if tablero[y][x] == 0:
                pygame.draw.rect(pantalla, COLOR_BLANCO, (x*100, y*100, 100, 100))
            elif tablero[y][x] == 1:
                pygame.draw.circle(pantalla, COLOR_ROJO, (x*100+50, y*100+50), 45)
            elif tablero[y][x] == 2:
                pygame.draw.circle(pantalla, COLOR_AMARILLO, (x*100+50, y*100+50), 45)

def comprobar_victoria():
    global partida_finalizada
    global partidas_rojo
    global partidas_amarillo

    # Comprobamos si hay empate
    if all(tablero[0][x] != 0 for x in range(7)):
        mostrar_mensaje("¡Empate!")
        partida_finalizada = True
        return

    # Comprobamos si hay victoria
    for x in range(7):
        for y in range(6):
            if tablero[y][x] != 0:
                # Comprobamos horizontal
                if x < 4 and tablero[y][x] == tablero[y][x+1] == tablero[y][x+2] == tablero[y][x+3]:
                    mostrar_ganador(tablero[y][x])
                    partida_finalizada = True
                    return
                # Comprobamos vertical
                if y < 3 and tablero[y][x] == tablero[y+1][x] == tablero[y+2][x] == tablero[y+3][x]:
                    mostrar_ganador(tablero[y][x])
                    partida_finalizada = True
                    return
                # Comprobamos diagonal \
                if x < 4 and y < 3 and tablero[y][x] == tablero[y+1][x+1] == tablero[y+2][x+2] == tablero[y+3][x+3]:
                    mostrar_ganador(tablero[y][x])
                    partida_finalizada = True
                    return
                # Comprobamos diagonal /
                if x < 4 and y > 2 and tablero[y][x] == tablero[y-1][x+1] == tablero[y-2][x+2] == tablero[y-3][x+3]:
                    mostrar_ganador(tablero[y][x])
                    partida_finalizada = True
                    return

def mostrar_ganador(jugador):
    global partidas_rojo
    global partidas_amarillo
    if jugador == 1:
        partidas_rojo += 1
        mostrar_mensaje("¡Ha ganado el jugador Rojo!")
    else:
        partidas_amarillo += 1
        mostrar_mensaje("¡Ha ganado el jugador Amarillo!")

def reiniciar_partida():
    global tablero
    global turno
    global partida_finalizada

    tablero = [[0 for x in range(7)] for y in range(6)]
    turno = 1
    partida_finalizada = False

def resetear_contadores():
    global partidas_rojo
    global partidas_amarillo

    partidas_rojo = 0
    partidas_amarillo = 0
    reiniciar_partida()

def mostrar_mensaje(mensaje):
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Conecta 4", mensaje)
    root.destroy()

def main():
    global pantalla
    global turno

    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Conecta 4")
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == MOUSEBUTTONDOWN:
                if not partida_finalizada:
                    x, y = pygame.mouse.get_pos()
                    columna = x // 100
                    for i in range(5, -1, -1):
                        if tablero[i][columna] == 0:
                            tablero[i][columna] = turno
                            comprobar_victoria()
                            turno = 3 - turno  # Cambia de turno: 1 -> 2, 2 -> 1
                            break
            if evento.type == KEYDOWN:
                if evento.key == K_r:
                    reiniciar_partida()
                if evento.key == K_c:
                    resetear_contadores()

        pantalla.fill(COLOR_FONDO)
        dibujar_tablero()
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()

# Interfaz grafica
root = Tk()
root.title("Conecta 4")
root.geometry("300x200")

frame = Frame(root)
frame.pack(pady=20)

boton_reiniciar = Button(frame, text="Reiniciar Partida", command=reiniciar_partida)
boton_reiniciar.grid(row=0, column=0, padx=10)

boton_resetear = Button(frame, text="Resetear Contadores", command=resetear_contadores)
boton_resetear.grid(row=0, column=1, padx=10)

root.mainloop()
