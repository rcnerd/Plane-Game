import sys, pygame, math, random
from Thing import Thing

class Block(Thing):
    def __init__(self, image, pos=[0,0]):
        Thing.__init__(self, image, pos)

class BigBlock(Block):
    def __init__(self, image, pos=[0,0]):
        Block.__init__(self, image, pos)
        self.image = pygame.image.load("Pictures/Blocks, and background/Crates/LargeCrate.png")
        self.image = pygame.transform.scale(self.image, [50*9,50*9])
        self.rect = self.image.get_rect(center = pos)
