import pygame
import constants
import player as p

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = p.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(constants.GAME_FPS)/1000

        screen.fill(pygame.Color("black"))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()