from circleshape import CircleShape
from pygame import Vector2, draw, Color

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        draw.circle(screen, Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
