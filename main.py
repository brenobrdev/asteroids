import pygame
import constants
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    ast = Asteroid(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, 20)
    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    # for implementation test only:
    ast.velocity = pygame.Vector2(17, 17)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(constants.GAME_FPS)/1000

        screen.fill(pygame.Color("black"))

        updatables.update(dt)

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()