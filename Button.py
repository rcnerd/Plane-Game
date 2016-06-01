import sys, pygame, math, random
from Block import Block

class Button(Block):
    def __init__(self, image, symbol, pos=[0,0], blockSize = [50,50]):
        Block.__init__(self, image, symbol, pos, blockSize)
        
    def wasClicked(self, mouseLocation = [0,0]):
        pass
    
    def isClicked(self, pt):
        if pt[0] > self.rect.left and pt[0] < self.rect.right:
            if pt[1] > self.rect.top and pt[1] < self.rect.bottom:
                return True
        return False
