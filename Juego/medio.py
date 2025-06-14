import pygame
import os
import creditos  # Importamos el archivo de créditos

def mostrar_animacion_con_pantalla_negra():
    """Función que ejecuta la animación con sprites y pantalla negra gradual."""
    # Inicialización de Pygame
    pygame.init()

    # Dimensiones de la ventana
    ANCHO = 1280
    ALTO = 720
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Animación con Pantalla Negra Gradual")

    # Cargar todos los sprites desde la carpeta 'delfin' con el formato adecuado
    sprites = []
    for i in range(39):  # Nombres de los sprites: sprite_00.png, sprite_01.png, ..., sprite_38.png
        sprite_path = os.path.join("delfin", f"sprite_{i:02d}.png")
        sprite = pygame.image.load(sprite_path).convert_alpha()
        sprites.append(sprite)

    # Variables de control
    reloj = pygame.time.Clock()
    index_sprite = 0
    velocidad_animacion = 8  # Velocidad de la animación (frames por segundo)
    opacidad_negra = 0  # Valor inicial de opacidad para la pantalla negra
    oscurecer_velocidad = 3  # Velocidad de oscurecimiento
    running = True

    # Bucle principal de la animación
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        # Limpiar la pantalla con el fondo negro
        ventana.fill((0, 0, 0))

        # Mostrar el sprite actual, si no hemos llegado al final
        if index_sprite < len(sprites):
            ventana.blit(sprites[index_sprite], 
                         (ANCHO // 2 - sprites[index_sprite].get_width() // 2, 
                          ALTO // 2 - sprites[index_sprite].get_height() // 2))
            index_sprite += 1  # Pasamos al siguiente sprite

            # Aumentar la opacidad de la pantalla negra gradualmente
            if opacidad_negra < 255:
                opacidad_negra += oscurecer_velocidad

        # Dibujar la capa negra con la opacidad actual
        capa_negra = pygame.Surface((ANCHO, ALTO))
        capa_negra.fill((0, 0, 0))
        capa_negra.set_alpha(opacidad_negra)
        ventana.blit(capa_negra, (0, 0))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de la animación
        reloj.tick(velocidad_animacion)

        # Terminar el bucle cuando todos los sprites se hayan mostrado y la pantalla esté completamente negra
        if opacidad_negra >= 255 and index_sprite >= len(sprites):
            running = False

    # Cerrar Pygame
    pygame.quit()

    # Llamar a los créditos después de la animación
    creditos.mostrar_creditos()  # Asegúrate de que esta función exista en el archivo 'creditos.py'

# Condición para ejecutar como programa independiente
if __name__ == "__main__":
    mostrar_animacion_con_pantalla_negra()