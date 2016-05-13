import sys, pygame, math, random
from Thing import *
from Block import *
from Button import *
from Booster import *
from Coin import *
from Spike import *
from Player import *
from Level import *
pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height
 
bgColor = r,g,b = 135, 206, 235

screen = pygame.display.set_mode(size)

blocks = pygame.sprite.Group()
buttons = pygame.sprite.Group()
gamePieces = pygame.sprite.Group()
actionGamePieces = pygame.sprite.Group()
boosters = pygame.sprite.Group()
coins = pygame.sprite.Group()
spikes = pygame.sprite.Group()
players = pygame.sprite.Group()
pointers = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Block.containers = (blocks, gamePieces, all)
Player.containers = (players, all)
Coin.containers = (coins, gamePieces, actionGamePieces, all)
Pointer.containers = (pointers, all)

level = Level("Levels/Level1.layout")

player = level.player

startup = False
arrowKeyPressed = False

cc = 0
#Pointer("Pictures/Pointer.png", [780, 4575], [-320, 0])
ground = 6*50

while True:
    while startup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        #foward
        if player.rect.left <  500:
            player.speed = [2,0]
            player.staticMove() 
        
        #tip down start scroll    
        elif player.rect.left >= 500 and player.rect.bottom < 600:
            self.previousTilt = self.tilt
            self.tilt = -45
            player.staticTilt()
            player.speed = [3,3]#vertish[3,3]
            
        #foward at bottom    
        elif player.rect.bottom >= 600 and player.vertPos[0] < 75:
            self.previousTilt = self.tilt
            self.tilt = 0
            player.staticTilt()
            player.virtSpeed = [4,0]
            player.virtPos[0] += player.virtSpeed[0]
            player.virtPos[1] += player.virtSpeed[1]
            
        #elif player.virtPos[0] >= 75 and player.rect.top > 300:
            #player.staticTilt(45)
            #player.speed = [0,-3]
            #player.virtSpeed = [3,-3]
            #gamePieceSpeed = [-3,0]
            #player.virtPos[0] += player.virtSpeed[0]
            #player.virtPos[1] += player.virtSpeed[1]
            #player.staticMove()
            #print "up!"
            #for c in gamePieces:
                #c.playerDynamicMove(gamePieceSpeed)
            
        #elif player.rect.top <= 300 and player.rect.left < 1100:
            #player.staticTilt(0)
            #player.speed = [4,0]
            #player.staticMove()
            #player.rect.top = 300
        
        #elif player.rect.left > 1100:
            #startup = False
            
        
        
        
        all.update(size,
                player.speed,
                player.didStaticMove())
                
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

    player.speed = [5,0]
    player.place([width/2, height/2])
    while not startup and player.fuelLevel > 0:
        ground += -player.speed[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.fly("fly up")
                    arrowKeyPressed = True
                elif event.key == pygame.K_DOWN:
                    player.fly("fly down")
                    arrowKeyPressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.fly("fly straight")
                    arrowKeyPressed = True
                elif event.key == pygame.K_DOWN:
                    player.fly("fly straight")
                    arrowKeyPressed = True
                
        if player.virtPos[0]%50 == 0:
            for y in range(75, 254*50, 50):
                y += -2000
                gamePiece = random.randint(0, 1000)
                if gamePiece == 0 or gamePiece == 1 or gamePiece == 2 or gamePiece == 3 or gamePiece == 4 or gamePiece == 5 or gamePiece == 6 or gamePiece == 7 or gamePiece == 8 or gamePiece == 9:
                    Coin(["Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin1.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin2.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin3.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin4.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin5.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin6.png"], "0",
                            [1100, y])
                    #print y, gamePieces.sprites()[-1].kind
                elif gamePiece == 10:
                    BigBlock("Pictures/Blocks, and background/BadCloud.png", "C",
                            [1500, y])                
                #elif gamePiece == 4:
                    #Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "^",
                            #[1100, y])
        
        #for c in coins:
            #if cc == 0:
                #cc = c
            #elif cc not in coins:
                #cc = 0
            #else:
                #pass
                #print cc.rect.center, cc.virtPos
                
        
        playersHit_gamePieces = pygame.sprite.groupcollide(players, gamePieces, False, False)
        actionPieceHit_blocks = pygame.sprite.groupcollide(actionGamePieces, blocks, False, False)
        
        for p in playersHit_gamePieces:
            for piece in playersHit_gamePieces[p]:
                if p.collideBlock(piece):
                    pass
                    
        if player.virtPos[1] >= 50000 - (player.virtPos[0] + 200):
            r,b,g = 250,110,110
                    
        for coin in coins:
            if coin.rect.center[1] > ground:
                coin.kill()
        
        all.update(size,
                player.speed,
                player.didStaticMove)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        #print clock.get_fps()
