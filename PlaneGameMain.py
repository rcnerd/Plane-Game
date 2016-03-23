import sys, pygame, math, random
from Object import *
from Block import *
from Button import *
from Booster import *
from Coin import *
from Spike import *
from Player import *
pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 800
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

blocks = pygame.sprite.Group()
buttons = pygame.sprite.Group()
gamePeices = pygame.sprite.Group()
boosters = pygame.sprite.Group()
coins = pygame.sprite.Group()
spikes = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()
print "I exist"
