import sys, pygame, math, random
from Thing import Thing

class Block(Thing):
    def __init__(self, image, symbol, pos=[0,0]):
        Thing.__init__(self, image, pos)
        self.symbol = symbol
        
        self.kind = "regular block"

class BigBlock(Block):
    def __init__(self, image, symbol, pos=[0,0]):
        Block.__init__(self, image, symbol, pos)
        self.image = pygame.image.load("Pictures/Blocks, and background/Crates/LargeCrate.png")
        self.blockSize = [50*9,50*9]
        self.image = pygame.transform.scale(self.image, self.blockSize)
        self.rect = self.image.get_rect(center = pos)
        
        self.kind = "9x9 block"

class LongBlock(Block):
    def __init__(self, image, symbol, pos=[0,0]):
        Block.__init__(self, image, symbol, pos)
        self.image = pygame.image.load("Pictures/Blocks, and background/Crates/LongCrate.png")
        self.blockSize = [50*9,50]
        self.image = pygame.transform.scale(self.image, self.blockSize)
        self.rect = self.image.get_rect(center = pos)
        self.kind = "9x1 block"
