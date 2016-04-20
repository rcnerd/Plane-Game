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
boosters = pygame.sprite.Group()
coins = pygame.sprite.Group()
spikes = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Block.containers = (blocks, gamePieces, all)
Player.containers = (players, all)
Coin.containers = (coins, gamePieces, all)
#PlayerBall.containers = (players, all)

level = Level("Levels/Level1.layout")

print len(all.sprites())

player = level.player
print player.rect.center, player.rect

startup = False

gameX = 25
#gameY = 0

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
            player.staticTilt(-45)
            player.speed = [3,3]#vertish[3,3]
            
        #foward at bottom    
        elif player.rect.bottom >= 600 and player.vertPos[0] < 75:
            player.staticTilt(0)
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
                player.didStaticMove)
        
        print player.virtPos[0] < 70
        print player.virtPos, player.virtSpeed
        print "Startup", player.rect.bottom
        for c in gamePieces:
            pass
            #print c.rect.center
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

    player.speed = [5,0]
    player.place([width/2, height/2])
    while not startup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.staticTilt(45/2)
                    player.speed = [5 , -2]
                elif event.key == pygame.K_DOWN:
                    player.staticTilt(-45/2)
                    player.speed = [5 , 2]
                #elif event.key == pygame.K_LEFT:
                    #player.go("left")
                #elif event.key == pygame.K_RIGHT:
                    #player.go("right")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.staticTilt(0)
                    player.speed = [5 , 0]
                elif event.key == pygame.K_DOWN:
                    player.staticTilt(0)
                    player.speed = [5 , 0]
                #elif event.key == pygame.K_LEFT:
                    #player.go("stop left")
                #elif event.key == pygame.K_RIGHT:
                    #player.go("stop right")
        if gameX%50 == 0:
            for y in range(75, 254*50, 50):
                gamePiece = random.randint(0, 100)
                if gamePiece == 0:
                    Coin(["Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin1.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin2.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin3.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin4.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin5.png",
                            "Pictures/Game pieces/GoldCoinSprite/GoldCoinSprite/Coin6.png"], "0",
                            [1100, y])#+gameY])
                elif gamePiece == 1:
                    Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "!",
                            [1100, y])#+gameY])
                elif gamePiece == 2:
                    Block("Pictures/Blocks, and background/Crates/obj_crate002.png", "^",
                            [1100, y])#+gameY])
                if gamePiece <= 2: print all.sprites()[-1].rect.center, y, gamePiece
        #raw_input("> ")
        
        #playersHitBalls = pygame.sprite.groupcollide(players, balls, False, True)
        playersHitBlocks = pygame.sprite.groupcollide(players, blocks, False, False)
        #ballsHitBoundries = pygame.sprite.groupcollide(balls, boundries, False, False)
        #ballsHitBalls = pygame.sprite.groupcollide(balls, balls, False, False)
        
        for p in playersHitBlocks:
            for block in playersHitBlocks[p]:
                if p.collideBlock(block):
                    all.update(size,
                        player.speed,
                        player.didStaticMove)
                    player.speed = [5,0]
        
        #for ball in ballsHitBoundries:
            #for boundry in ballsHitBoundries[ball]:
                #ball.collideBoundry(boundry)
        
        #for ball1 in ballsHitBalls:
            #for ball2 in ballsHitBalls[ball1]:
                #ball1.collideBall(ball2)3
        
        all.update(size,
                player.speed,
                player.didStaticMove)
        gameX += player.speed[0]
        #gameY += player.speed[1]
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        print clock.get_fps(), len(all.sprites())



