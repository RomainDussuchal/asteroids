import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
       

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius,  width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        a =self.velocity.rotate(rand_angle)
        b =self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        

        for _ in range(0,2) : 
            if _ == 0 :
                asteroid = Asteroid(self.position.x, self.position.y, new_radius) 
                asteroid.velocity = a * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius) 
            asteroid.velocity = b * 1.2
       


   