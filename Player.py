import sys, pygame, math, random

class Player(pygame.sprite.Sprite):
    def __init__(self, images, pos=[0,0], speed = [3, 1]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.virtPos = [25,0]
        self.virtSpeed = [0,0]
        self.maxFuelLevel = 100
        self.fuelLevel = self.maxFuelLevel
        self.fuelUseRate = self.maxFuelLevel/(15*60) #15 seconds at 60 frames 
        
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
    
    def staticMove(self):
        self.rect = self.rect.move(self.speed)
        self.didStaticMove = True

    def staticTilt(self, angle):
        self.image = pygame.transform.rotate(self.images[0], angle)
        
    def update(*args):
        self = args[0]
        self.didStaticMove = False
        self.didBounceY = False

    def place(self, pos):
        self.rect.center = pos
        
    def fly(self, direction):
        if direction == "fly up":
            self.staticTilt(45/2)
            self.speed = [5 , -2]
        elif direction == "fly down":
            self.staticTilt(-45/2)
            self.speed = [5 , 2]
        elif direction == "fly straight":
            self.staticTilt(0)
            self.speed = [5 , 0]
        elif direction == "previous":
            self.speed = self.previousSpeed
    def move(self):
        pass
    
    def collideBlock(self, other):
        if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
            #self.didBounceX = True
            self.didBounceY = True
            #self.speedx = -self.speedx
            
            #print other.image
            if other.symbol == "_":
                self.previosSpeed = self.speed
                #self.previousTilt 
                self.staticTilt(0)
                self.speed = [0,1]
                return True
            elif other.symbol == "#":
                self.previosSpeed = self.speed
                self.staticTilt(0)
                self.speed = [0,-1]
                return True
            else:
                return False
        
            
