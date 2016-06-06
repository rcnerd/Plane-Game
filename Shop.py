import pygame, sys, math, random
from Block import *
from Button import *

class Shop():
    def __init__(self, lev):
        self.loadLevel(lev)
    
    def loadLevel(self, lev):
        file = open(lev, 'r')
        lines = file.readlines()
        file.close()
        
        blockSize = 100
        
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline+= c
            newlines += [newline]
        lines = newlines
        
        previousLine = 0
        chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#']
        buttons = ['1','2','3','4','5','6','7','8','9','0','<','p']
        for y, line in enumerate(lines):
            print y,line
            for x, c in enumerate(line):
                print "--->",x,c
                if c in chars:
                    if c == '#':
                        Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "#",
                            [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-9*100], [blockSize,blockSize])
                        print "don made a reg block"
                    else:
                        Block("Pictures/Blocks, and background/Letter_Blocks_01/Letter_Blocks_01/Letter_Blocks_01_Set_4_"+c+"_64x64.png", c,
                            [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-9*100], [blockSize,blockSize])
                        previousLine = line
                        print "don made a letter block"
                elif c in buttons:
                    Button("Pictures/Blocks, and background/Letter_Blocks_01/"+c+".png", c, previousLine,
                        [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-9*100], [blockSize,blockSize])
                    print "don made a Button"
