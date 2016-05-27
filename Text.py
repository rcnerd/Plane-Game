import sys, pygame, math, random
from Player import Player

class Text(pygame.sprite.Sprite):
    def __init__(self, text, location, screenSize):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.text = text
        
        font = pygame.font.Font(None, 36)
        self.image = font.render(text, 1, (200, 0, 0))
        self.rect = self.image.get_rect(center = location)
        print self.rect
