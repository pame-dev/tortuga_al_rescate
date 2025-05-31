import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
W, H = 600, 400
pantalla = pygame.display.set_mode((W, H))
pygame.display.set_caption("Imágenes de Vida")

# Cargar imágenes
imagenes_vida = {
    1: pygame.transform.scale(pygame.image.load("vidas/vida1.png"),(30,30)),
    2: pygame.transform.scale(pygame.image.load("vidas/vida2.png"),(60,30)),
    3: pygame.transform.scale(pygame.image.load("vidas/vida3.png"),(90,30)),
    4: pygame.transform.scale(pygame.image.load("vidas/vida4.png"),(120,30)),
    5: pygame.transform.scale(pygame.image.load("vidas/vida5.png"),(150,30)),
}

# Índice de la imagen actual
vida_actual = 1

# Bucle principal
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Cambiar la imagen de vida con las teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:  # Siguiente imagen
                vida_actual += 1
                if vida_actual > 5:
                    vida_actual = 5  # Limitar al máximo
            elif evento.key == pygame.K_DOWN:  # Imagen anterior
                vida_actual -= 1
                if vida_actual < 1:
                    vida_actual = 1  # Limitar al mínimo

    # Limpiar la pantalla
    pantalla.fill((0, 0, 0))

    # Mostrar la imagen correspondiente usando if
    if vida_actual == 1:
        pantalla.blit(imagenes_vida[1], (200, 100))
    elif vida_actual == 2:
        pantalla.blit(imagenes_vida[2], (200, 100))
    elif vida_actual == 3:
        pantalla.blit(imagenes_vida[3], (200, 100))
    elif vida_actual == 4:
        pantalla.blit(imagenes_vida[4], (200, 100))
    elif vida_actual == 5:
        pantalla.blit(imagenes_vida[5], (200, 100))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(30)
