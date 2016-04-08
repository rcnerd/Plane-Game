import sys, pygame, math, random

class Thing(pygame.sprite.Sprite):
    def __init__(self, image, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [50,50])
        self.rect = self.image.get_rect(center = pos)
        
        self.speed = 0

    def update(*args):
        self = args[0]
        playerSpeed = args[1]
        playerStatic = args[2] #game not happy with this line
        
        

    def move(self):
        self.rect = self.rect.move(self.speed)
