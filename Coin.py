import sys, pygame, math, random
from Thing import Thing

class Coin(Thing):
    def __init__(self, image, symbol, pos=[0,0]):
        Thing.__init__(self, image, pos)
        self.symbol = symbol
