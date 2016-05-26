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

        chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#']
        buttons = ['1','2','3','4','5','6','7','8','9','0','<','>']
        for y, line in enumerate(lines):
            print y,line
            for x, c in enumerate(line):
                print "--->",x,c
                if c in chars:
                    if c == '#':
                        Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "#",
                            [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)], [blockSize,blockSize])
                        print "don made a reg block"
                    else:
                        Block("Pictures/Blocks, and background/Letter_Blocks_01/Letter_Blocks_01/Letter_Blocks_01_Set_4_"+c+"_64x64.png", c,
                            [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)], [blockSize,blockSize])
                        print "don made a letter block"
                elif c in buttons:
                    Button("Pictures/Blocks, and background/Letter_Blocks_01/"+c+".png", c,
                        [blockSize*x+blockSize/2, blockSize*y+(blockSize/2)], [blockSize,blockSize])
                    print "don made a Button"
                #elif c == 'A':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'B':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'C':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'D':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'E':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'F':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'G':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'H':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'I':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'J':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'K':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'L':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'M':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])\
                #elif c == 'N':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'O':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'P':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'Q':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'R':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'S':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'T':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'U':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'V':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'w':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'X':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'Y':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == 'Z':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                         
                         
                #elif c == '1':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '2':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '3':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '4':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '5':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '6':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '7':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '8':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                #elif c == '9':
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "A",
                         #[blockSize*x+blockSize/2, blockSize*y+(blockSize/2)-12100])
                    
            
                
