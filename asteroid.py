from circleshape import CircleShape
from pygame import Vector2, draw, Color

import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        draw.circle(screen, Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        new_angle_delta = random.uniform(20, 50)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_1.velocity = self.velocity.rotate(new_angle_delta) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-new_angle_delta) * 1.2
        