import pygame
from constants import *
from logger import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import sys
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
