import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Board") # el texto que sale en la ventana del juego

# Define initial settings
drawing = False
color = (0, 0, 0)
radius = 5
background_color = (255, 255, 255)
screen.fill(background_color)
font = pygame.font.SysFont('Calibri', 18)

# Cambiar de color con teclas
colors = {
    pygame.K_r: (255, 0, 0), # rojo
    pygame.K_g: (0, 255, 0), # verde
    pygame.K_b: (0, 0, 255), #azul
    pygame.K_k: (0, 0, 0), # negro
    pygame.K_w: (255, 255, 255) # blanco
}

#Crear menú con instrucciones/teclas

def draw_instructions():
    instructions = [
        "R - Red   G - Green   B - Blue   K - Black   W - White",
        "C - Limpiar lienzo",
        "Q - Salir"
    ]
    for i, line in enumerate(instructions):
        # convierte la cadena de cada línea en una imagen de Pygame
        text = font.render(line, True, (50, 50, 50))
        # blit = copiar la imagen (text) en la pantalla
        # cada línea se imprime 20 pixeles más abajo que la anterior
        screen.blit(text, (10, 10 + i * 20))

# Main loop

while True:
    for event in pygame.event.get():
        # pygame.quit() es lo opuesto a pygame.init(), reinicia todo y sale del juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Start/stop drawing with mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Change color with keys or clear screen
        elif event.type == pygame.KEYDOWN:
            if event.key in colors:
                # cambiar de color con teclas
                color = colors[event.key]
            elif event.key == pygame.K_c:
                # borra todo el dibujo con C
                screen.fill(background_color)
            elif event.key == pygame.K_q:
                # salimos del juego al presionar la tecla Q
                pygame.quit()
                sys.exit()

    # Draw on the screen
    if drawing:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, pos, radius)

# Para dibujar con Pygame
# pygame.draw.circle(surface, color, center, radius, width=0)
# también tiene opción de - line(), rect(), ellipse(), polygon()
# ejemplo: pygame.draw.polygon(screen,'blue',[(100,100),(100,200),(200,300)],0)

    draw_instructions()
    pygame.display.flip()