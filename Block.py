import sys, pygame, math, random
from Thing import Thing

class Block(Thing):
    def __init__(self, image, pos=[0,0]):
        Thing.__init__(self, image, pos)
