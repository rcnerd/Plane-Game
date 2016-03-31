import pygame, sys, math, random
from Block import *
from Player import *
#from Wall import *
#from PlayerBall import *

class Level():
    def __init__(self, lev):
        self.loadLevel(lev)
    
    def loadLevel(self, lev):
        file = open(lev, 'r')
        lines = file.readlines()
        file.close()
        
        blockSize = 50
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
                    Block("Pictures/Blocks, and background/Crates/obj_crate002.png", 
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                if c == 'A':
                    Block("Pictures/Blocks, and background/Crates/slope.png", 
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                
                if c == '/':
                    Block("Pictures/Blocks, and background/Crates/ramp.png", 
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                         
                #if c == '_':
                    #Block("Pictures/Blocks, and background/Crates/plank.png", 
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-11900])
                         
                if c == '@':
                    self.player = Player(["Pictures/Player/Biplane.png"],
                            [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100+12])
