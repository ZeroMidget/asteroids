import pygame
from circleshape import CircleShape
from constants import *
    
class Shot(CircleShape):
    def __init__(self, x, y, velocity):
      super().__init__(x, y, SHOT_RADIUS)
      self.velocity = velocity

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen,"white",center,self.radius,2)

    def update(self,dt):
       self.position += self.velocity*dt