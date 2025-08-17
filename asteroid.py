import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen,"white",center,self.radius,2)

    def update(self,dt):
       self.position = self.position+(self.velocity*dt)
    
    def split(self):
      print(f"Splitting asteroid with radius {self.radius}")
      self.kill()
       
      if self.radius <= ASTEROID_MIN_RADIUS:
        return
       
      else:
          random_angle = random.uniform(20,50)
          old_radius = self.radius
          new_radius = old_radius - ASTEROID_MIN_RADIUS
          split_velocity1 = self.velocity.rotate(random_angle)*1.2
          split_velocity2 = self.velocity.rotate(-random_angle)*1.2
          AsteroidSplit1 = Asteroid(self.position.x, self.position.y,new_radius)
          AsteroidSplit1.velocity = split_velocity1
          AsteroidSplit2 = Asteroid(self.position.x, self.position.y,new_radius)
          AsteroidSplit2.velocity = split_velocity2