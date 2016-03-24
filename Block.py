import sys, pygame, math, random
from Object import Object
class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos=[0,0]):
        Object.__init__(self, image, pos=[0,0])
