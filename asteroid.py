from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        new_asteroid_1_vel = self.velocity.rotate(new_angle)
        new_asteroid_2_vel = self.velocity.rotate(new_angle*-1)
        new_asteroid_1 = Asteroid(int(self.position.x), int(self.position.y), self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid_2 = Asteroid(int(self.position.x), int(self.position.y), self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid_1.velocity += new_asteroid_1_vel * 1.2
        new_asteroid_2.velocity += new_asteroid_2_vel * 1.2