# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Tworzenie okna
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Tworzenie zegara i zmiennej delta time
    clock = pygame.time.Clock()
    dt = 0  # czas między klatkami (w sekundach)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Główna pętla gry
    while True:
        # Obsługa zdarzeń (np. zamknięcie okna)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Wyjście z funkcji main kończy program

        # Wypełnianie ekranu kolorem czarnym (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        player.update(dt)         # aktualizacja gracza

        player.draw(screen)

        # Odświeżenie ekranu
        pygame.display.flip()

        # Ograniczenie do 60 FPS i zapisanie delta time (w sekundach)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()