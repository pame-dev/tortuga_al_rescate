import pygame
import sys
import json
import historia
import controls
import configuracion
import creditos
# Cargar el archivo JSON con las configuraciones de idiomas

# Nivel de volumen inicial
volumen = 0.5
muteado = False

def ajustar_volumen(valor):
    """Ajusta el volumen del sonido globalmente."""
    global volumen, muteado
    if not muteado:
        volumen = max(0.0, min(1.0, volumen + valor))
        pygame.mixer.music.set_volume(volumen)

def toggle_mute():
    """Activa o desactiva el mute."""
    global muteado
    muteado = not muteado
    pygame.mixer.music.set_volume(0 if muteado else volumen)

def mostrar_configuracion(pantalla, reloj):


    # Cargar imagen de fondo
    fondo = pygame.image.load("imagenes/configuracion.jpeg").convert()
    fondo = pygame.transform.scale(fondo, pantalla.get_size())

    # Cargar imágenes de los botones
    boton_controles_img = pygame.transform.scale(pygame.image.load("botones/control1.png"), (100, 80)).convert_alpha()
    boton_controles_img_presionado = pygame.transform.scale(pygame.image.load("botones/control2.png"), (100, 80)).convert_alpha()
    boton_historia_img = pygame.transform.scale(pygame.image.load("botones/libro1.png"), (100, 80)).convert_alpha()
    boton_historia_img_presionado = pygame.transform.scale(pygame.image.load("botones/libro2.png"), (100, 80)).convert_alpha()
    boton_mute_img = pygame.transform.scale(pygame.image.load("botones/nada1.png"), (100, 80)).convert_alpha()
    boton_mute_img_presionado = pygame.transform.scale(pygame.image.load("botones/nada2.png"), (100, 80)).convert_alpha()
    boton_regresar_img = pygame.transform.scale(pygame.image.load("botones/regresar1.png"), (100, 80)).convert_alpha()
    boton_regresar_img_presionado = pygame.transform.scale(pygame.image.load("botones/regresar2.png"), (100, 80)).convert_alpha()

    # Dimensiones y posiciones de los botones
    W, H = pantalla.get_size()
    boton_controles_rect = boton_controles_img.get_rect(center=(W // 2, H // 2 - 175))
    boton_mute_rect = boton_mute_img.get_rect(center=(W // 2, H // 2 ))
    boton_historia_rect = boton_historia_img.get_rect(center=(W // 2, H // 2 + 175 ))
    boton_regresar_rect = boton_regresar_img.get_rect(topleft=(10, 10))  # Colocado en la esquina superior izquierda

    # Bucle de configuración
    configurando = True
    while configurando:
        pantalla.blit(fondo, (0, 0))  # Dibujar la imagen de fondo

        # Obtener la posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_controles_rect.collidepoint(evento.pos):  # Clic en "Controles"
                    controls.mostrar_controls(pantalla, reloj)  # Llamar a la función en controls.py
                elif boton_historia_rect.collidepoint(evento.pos):  # Clic en "Historia"
                    historia.mostrar_historia(pantalla)  # Llamar a la función en historia.py
                elif boton_mute_rect.collidepoint(evento.pos):  # Clic en "Mute"
                    toggle_mute()
                elif boton_regresar_rect.collidepoint(evento.pos):  # Clic en "Regresar"
                    configurando = False  # Salir de la configuración
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Salir al menú principal con ESC
                    configurando = False
                elif evento.key == pygame.K_UP:  # Subir volumen
                    ajustar_volumen(0.1)
                elif evento.key == pygame.K_DOWN:  # Bajar volumen
                    ajustar_volumen(-0.1)
                elif evento.key == pygame.K_m:  # Mute
                    toggle_mute()

        # Cambiar imágenes al pasar el mouse por encima
        if boton_controles_rect.collidepoint(mouse_pos):
            pantalla.blit(boton_controles_img_presionado, boton_controles_rect.topleft)
        else:
            pantalla.blit(boton_controles_img, boton_controles_rect.topleft)
        if boton_historia_rect.collidepoint(mouse_pos):
            pantalla.blit(boton_historia_img_presionado, boton_historia_rect.topleft)
        else:
            pantalla.blit(boton_historia_img, boton_historia_rect.topleft)

        # Cambiar la imagen del botón mute según el estado
        if boton_mute_rect.collidepoint(mouse_pos) or muteado:
            pantalla.blit(boton_mute_img_presionado, boton_mute_rect.topleft)
        else:
            pantalla.blit(boton_mute_img, boton_mute_rect.topleft)

        # Botón regresar
        if boton_regresar_rect.collidepoint(mouse_pos):
            pantalla.blit(boton_regresar_img_presionado, boton_regresar_rect.topleft)
        else:
            pantalla.blit(boton_regresar_img, boton_regresar_rect.topleft)

        # Actualizar la pantalla
        pygame.display.flip()
        reloj.tick(60)
