import sys, pygame, math, random

class Player(pygame.sprite.Sprite):
    def __init__(self, images, pos=[0,0], speed = [3, 1]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.virtPos = [0,0]
        self.virtSpeed = [0,0]
        
        self.images = []
        for image in images:
            self.images += [pygame.transform.scale(pygame.image.load(image), [50,25])]#[1083/20,524/20])]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = pos)
        print pos, self.rect
        
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.timer = 0
        self.timerMax = .25* 60
        
        #self.rect = self.rect.move(pos)
        self.didStaticMove = False
    
    def staticMove(self):
        self.rect = self.rect.move(self.speed)
        self.didStaticMove = True

    def staticTilt(self, angle):
        self.image = pygame.transform.rotate(self.images[0], angle)
        
    def update(*args):
        self = args[0]
        self.didStaticMove = False

    def place(self, pos):
        self.rect.center = pos
        
    def move(self):
        pass
