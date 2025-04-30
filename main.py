# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Grupy do aktualizacji i rysowania
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Tworzenie okna
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Tworzenie zegara i zmiennej delta time
    clock = pygame.time.Clock()
    dt = 0  # czas między klatkami (w sekundach)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    # Główna pętla gry
    while True:
        # Obsługa zdarzeń (np. zamknięcie okna)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Wyjście z funkcji main kończy program

        # Wypełnianie ekranu kolorem czarnym (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        updatable.update(dt) # aktualizacja wszystkich obiektów

        # Sprawdzenie kolizji gracza z asteroidami
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        # Wykrywanie kolizji: pociski vs asteroidy
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()      # Usunięcie pocisku
                    asteroid.split()  # rozdzielenie asteroidy

        for obj in drawable:  # rysowanie każdego obiektu
            obj.draw(screen)

        # Odświeżenie ekranu
        pygame.display.flip()

        # Ograniczenie do 60 FPS i zapisanie delta time (w sekundach)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()