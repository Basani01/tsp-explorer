import pygame
import math

class City:

    def __init__(self, x, y, Indx, name):
        self.y=y
        self.x=x
        self.name=name
        self.Indx=Indx
        self.radius= 7

    def draw(self, screen):
       pygame.draw.circle(screen, (255, 69, 0), (self.x, self.y), self.radius)
       font = pygame.font.SysFont(None, 20)
       text = font.render(str(self.name), True, (255, 255, 255))
       screen.blit(text, (self.x + 10, self.y))

    def isclicked(self, pos):
        dx = self.x - pos[0]
        dy = self.y - pos[1]
        return dx * dx + dy * dy <= self.radius * self.radius

    def get_pos(self):
        return (self.x, self.y)

    
    def distance_to(self, anothercity):
     dx = self.x - anothercity.x
     dy = self.y - anothercity.y
     return math.hypot(dx, dy)
    