import pygame
import sys

import settings

pygame.init()

screen = pygame.display.set_mode(
    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT),
    settings.WINDOW_FLAGS #создаем игровое окно
)

pygame.display.set_caption(settings.GAME_TITLE)

clock = pygame.time.Clock()

title_font = pygame.font.SysFont("Arial", 48, bold=True)
info_font = pygame.font.SysFont("Arial", 24)

BACKGROUND_COLOR = (112, 158, 75)
TEXT_COLOR = (255, 255, 255)

def draw_game():
    screen.fill(BACKGROUND_COLOR)
    title = title_font.render(
        settings.GAME_TITLE,
        True,
        TEXT_COLOR
    )

    screen.blit(
        title,
        (settings.SCREEN_WIDTH // 2 - title.get_width() // 2, 100)
    )

    info = info_font.render(
        "Welcome to the African Savanna!",
        True,
        TEXT_COLOR
    )

    screen.blit(
        info,
        (settings.SCREEN_WIDTH // 2 - info.get_width() // 2, 180)
    )

    running = True

    while running:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False

        draw_game()

        pygame.display.flip()

        clock.tick(settings.FPS)


pygame.quit()
sys.exit

