import pygame, sys, math, random
from Block import *
from Player import *

class Level():
    def __init__(self, lev):
        self.loadLevel(lev)
    
    def loadLevel(self, lev):
        file = open(lev, 'r')
        lines = file.readlines()
        file.close()
        
        blockSize = 50
        
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline+= c
            newlines += [newline]
        lines = newlines

            
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "#",
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                elif c == 'N':
                    BigBlock("Pictures/Blocks, and background/Crates/LargeCrate.png", "N",
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                elif c == 'L':
                    LongBlock("Pictures/Blocks, and background/Crates/obj_crate002.png", "N",
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                elif c == 'A':
                    Block("Pictures/Blocks, and background/Crates/slope.png", "A",
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                
                elif c == '/':
                    Block("Pictures/Blocks, and background/Crates/ramp.png", "/",
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                         
                elif c == '_':
                    Block("Pictures/Blocks, and background/Crates/plank.png", "_",
                         [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                         
                elif c == '@':
                    self.player = Player(["Pictures/Player/Biplane.png"],
                            [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100+12])
