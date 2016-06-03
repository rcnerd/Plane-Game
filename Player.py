import sys, pygame, math, random

class Player(pygame.sprite.Sprite):
    def __init__(self, images, pos=[0,0], previousBankAccount = 0, playerMaxFuelTime = 15, speed = [3, 1]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.virtPos = [25,0]
        self.virtSpeed = [0,0]
        self.maxFuelLevel = 100000
        self.fuelLevel = self.maxFuelLevel
        self.fuelUseRate = self.maxFuelLevel/(playerMaxFuelTime*60) #15 seconds at 60 frames 
        #print self.fuelUseRate
        self.bankAmount = previousBankAccount
        
        self.images = []
        for image in images:
            self.images += [pygame.transform.scale(pygame.image.load(image), [50,25])]#[1083/20,524/20])]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = pos)
        #print pos, self.rect
        
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.timer = 0
        self.timerMax = .25* 60
        
        #self.rect = self.rect.move(pos)
        self.didStaticMove = False
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.previousSpeed = [0,0]
        self.previousTilt = 0
        self.tilt = 0
    
    def staticMove(self):
        self.rect = self.rect.move(self.speed)
        self.didStaticMove = True

    def staticTilt(self):
        self.image = pygame.transform.rotate(self.images[0], self.tilt)
        
    def update(*args):
        self = args[0]
        self.staticTilt()
        self.didStaticMove = False
        self.didBounceY = False
        self.virtPos[0] += self.speed[0]
        self.virtPos[1] += self.speed[1]
        self.fuelLevel += -self.fuelUseRate

    def place(self, pos):
        self.rect.center = pos
        
    def fly(self, direction):
        if direction == "fly up":
            self.previousTilt = self.tilt
            self.tilt = 45/2
            self.speed = [5 , -2]
        elif direction == "fly down":
            self.previousTilt = self.tilt
            self.tilt = -45/2 
            self.speed = [5 , 2]
        elif direction == "fly straight":
            self.previousTilt = self.tilt
            self.tilt = 0
            self.speed = [5 , 0]
        elif direction == "previous":
            self.speed = self.previousSpeed
            self.tilt = self.previousTilt
    def move(self):
        pass
    
    def collideBlock(self, other):
        if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
            #self.didBounceX = True
            self.didBounceY = True
            
            if other.symbol == "_":
                self.fly("fly down")
                return True
            elif other.symbol == "#":
                self.fly("fly up")
                return True
            elif other.symbol == "0":
                self.bankAmount += 25
                other.kill()
                print self.bankAmount
                return True
            elif other.symbol == "^":
                self.fuelLevel = self.maxFuelLevel-1
                other.kill()
                print self.fuelLevel
                return True
            else:
                return False
        
            
