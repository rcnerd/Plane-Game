import sys, pygame, math, random
from Player import Player

class Text(pygame.sprite.Sprite):
    def __init__(self, text, location, screenSize, color = (0,0,0)):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.text = text
        self.speed =[0,0] 
        
        font = pygame.font.Font(None, 72)
        self.image = font.render(text, 1, color)
        self.rect = self.image.get_rect(center = location)
        #print self.rect
    
    def move(self):
        self.rect = self.rect.move(self.speed)
