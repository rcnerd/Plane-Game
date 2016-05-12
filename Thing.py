import sys, pygame, math, random

class Thing(pygame.sprite.Sprite):
    def __init__(self, image, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.blockSize = [50,50]
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, self.blockSize)
        self.rect = self.image.get_rect(center = pos)
        
        self.speed = [0,0]
        self.virtPos = [0,0]

    def update(*args):
        self = args[0]
        playerSpeed = args[2]
        self.speed[0] = -playerSpeed[0]
        self.speed[1] = -playerSpeed[1]
        self.move()
        if self.rect.center[0] < self.blockSize[0]/2*-1: #-1/2 block size so that we r + it is off screen
            self.kill()
            


    def move(self):
        self.rect = self.rect.move(self.speed)

    def collide(self, other):
        if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
            
            if other.symbol == "_":
                return True
            elif other.symbol == "#":
                return True
            else:
                return False

class Pointer(pygame.sprite.Sprite):
    def __init__(self, image, pos = [0,0], virtPos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.blockSize = [10,10]
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, self.blockSize)
        self.rect = self.image.get_rect(center = pos)
        
        self.virtPos = virtPos
