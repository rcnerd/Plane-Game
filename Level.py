import pygame, sys, math, random
from Block import *
#from Wall import *
#from PlayerBall import *

class Level():
    def __init__(self, lev):
        self.loadLevel(lev)
    
    def loadLevel(self, lev):
        file = open(lev, 'r')
        lines = file.readlines()
        file.close()

        #ballOdds = 3
        #ballMax = 10
        #ballCount = 0
        
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline+= c
            newlines += [newline]
        lines = newlines

        for line in lines:
            print line
            
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    Block("Pictures\Blocks, and background\Crates\obj_crate002.png", 
                         [50*x+25,50*y+25])
                #if c == 'o':
                    #if ballCount < ballMax:
                        #if random.randint(1, ballOdds) == 1:
                            #Ball(["ball.png"], [5,5], [25*x+12,25*y+12])
                
                #if c == '@':
                    #self.player = PlayerBall("pBall.png",[6,6],[25*x+12,25*y+12])
