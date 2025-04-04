from circleshape import CircleShape
import constants
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # screen is of type Surface
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), 2)

    def update(self, dt):
        self.rotate(dt)
        self.move(dt)
    
    def rotate(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= constants.PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += self.forward * constants.PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= self.forward * constants.PLAYER_SPEED * dt