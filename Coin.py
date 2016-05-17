import sys, pygame, math, random
#from Thing import Thing

class Coin(pygame.sprite.Sprite):
    def __init__(self, images, symbol, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        image = images[0]
        #Thing.__init__(self, image, pos)
        self.symbol = symbol
        self.blockSize = [50,50]
        self.speed = [0,0]
        self.virtPos = [0,0]
        self.images = []
        for image in images:
            self.images += [pygame.transform.scale(pygame.image.load(image), [50,50])]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = pos)
        
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.timer = 0
        self.timerMax = .12* 60
        
    def update(*args):
        self = args[0]
        playerSpeed = args[2]
        self.speed[0] = -playerSpeed[0]
        self.speed[1] = -playerSpeed[1]
        self.move()
        if self.rect.center[0] < self.blockSize[0]/2*-1 +10: #-1/2 block size so that we r + it is off screen
            self.kill()
            
        if self.timer < self.timerMax:
            self.timer += 1
        else:
            self.timer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]

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
