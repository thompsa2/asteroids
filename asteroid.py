import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        #save info on the parent asteroid
        parent_position = self.position
        parent_velocity = self.velocity
        parent_radius = self.radius

        #kill the parent asteroid
        self.kill()

        #check if the parent was big enough to spawn children
        if parent_radius <= ASTEROID_MIN_RADIUS:
            #if no, done
            return
        
        #if yes, spawn 2 new children asteroids
        #roll a random offset angle between 20 & 50 degrees
        offset_angle = random.uniform(20, 50)

        child1_velocity = parent_velocity.rotate(offset_angle)
        child2_velocity = parent_velocity.rotate(-offset_angle)

        child_radius = parent_radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(parent_position.x, parent_position.y, child_radius)
        child1.velocity = child1_velocity * 1.2

        child2 = Asteroid(parent_position.x, parent_position.y, child_radius)
        child2.velocity = child2_velocity * 1.2




        
        
        
        