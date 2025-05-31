import pygame
import os
import creditos  # Importamos el archivo de créditos
pygame.mixer.init()

def mostrar_animacion():
    """Función que ejecuta la animación con sprites de 'sprite_00.png' hasta 'sprite_42.png'."""
    # Inicialización de Pygame
    pygame.init()

    # Dimensiones de la ventana
    ANCHO = 1280
    ALTO = 720
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Animación con Sprites")

    # Cargar todos los sprites desde la nueva ruta con el nuevo formato
    sprites = []
    for i in range(43):  # Nombres de los sprites: sprite_00.png, sprite_01.png, ..., sprite_42.png
        sprite_path = os.path.join("tortuga", f"sprite_{i:02d}.png")  # Formato con 2 dígitos
        sprite = pygame.image.load(sprite_path).convert_alpha()  # Cargar y mantener la transparencia
        sprites.append(sprite)

    # Variables de control
    reloj = pygame.time.Clock()
    index_sprite = 0
    velocidad_animacion = 8  # Velocidad de la animación (frames por segundo)
    running = True

    # Bucle principal de la animación
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        # Limpiar la pantalla con el fondo negro
        ventana.fill((0, 0, 0))

        # Si no hemos mostrado todos los sprites, mostramos el siguiente
        if index_sprite < len(sprites):
            # Dibujar el sprite actual
            ventana.blit(sprites[index_sprite], (ANCHO // 2 - sprites[index_sprite].get_width() // 2, ALTO // 2 - sprites[index_sprite].get_height() // 2))

            # Aumentar el índice del sprite
            index_sprite += 1  # Pasamos al siguiente sprite

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de la animación
        reloj.tick(velocidad_animacion)

        # Terminar el programa cuando todos los sprites hayan sido mostrados
        if index_sprite >= len(sprites):
            running = False

    # Cerrar Pygame
    pygame.quit()

    # Llamamos a la función de créditos después de la animación
    creditos.mostrar_creditos()  # Asumiendo que la función de mostrar créditos se llama `mostrar_creditos`

# Condición para ejecutar como programa independiente
if __name__ == "__main__":
    mostrar_animacion()
