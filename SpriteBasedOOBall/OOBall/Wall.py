import sys, pygame, math

class Wall(pygame.sprite.Sprite):
    def __init__(self, image, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [25,25])
        self.rect = self.image.get_rect(center = pos)

    def update(*args):
        pass
        
    
        
        
            
