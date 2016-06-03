import sys, pygame, math, random

class FuelGuage(pygame.sprite.Sprite):
    def __init__(self, maxFuel, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = []
        for i in range(0,110,10):
            self.images += [pygame.transform.scale(pygame.image.load("Pictures/Game pieces/"+str(i)+"fuel.png"), [24,70])]
        self.maxFuel = maxFuel
        print maxFuel
        self.currentFuel = maxFuel
        self.percentFuel = float(self.currentFuel)/float(self.maxFuel)*100
        
        self.frame = int(round(self.percentFuel/10))
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        
    def update(*args):
        self = args[0]
        self.currentFuel = args[4]
        
        self.percentFuel = float(self.currentFuel)/float(self.maxFuel)*100
        
        self.frame = int(round(self.percentFuel/10))
        self.image = self.images[self.frame]
