import sys, pygame, math, random
from Object import Object

class Block(Object):
    def __init__(self, image, pos=[0,0]):
        Object.__init__(self, image, pos=[0,0])
