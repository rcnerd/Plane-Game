import sys, pygame, math, random, time
from Thing import *
from Block import *
from Button import *
from Booster import *
from Coin import *
from Spike import *
from Player import *
from Level import *
from Cloud import *
from Shop import *
from Text import *
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
clouds = pygame.sprite.Group()
everyone = pygame.sprite.Group()
textBoxes = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Block.containers = (blocks, gamePieces, everyone, all)
Player.containers = (players, everyone, all)
Coin.containers = (coins, gamePieces, actionGamePieces, everyone, all)
Pointer.containers = (pointers, everyone, all)
Booster.containers = (boosters, gamePieces, actionGamePieces, everyone, all)
Cloud.containers = (clouds, everyone, all)
Button.containers = (buttons, everyone, all)
Text.containers = (textBoxes, everyone, all)


startup = True
shop = False
arrowKeyPressed = False

cc = 0 # used for picking a single object in a list see 192 ish
ground = 6*50
playerBankAmount = 0
playerMaxFuelTime = 15

while True:
    
    for person in everyone:
        person.kill()
    
    shop = Shop("Levels/Shop.layout")
    shopScroll = [0,0]
    
    
    
    bankAccountLevelTextL = Text("$"+str(playerBankAmount), [50,150], size, (100,200,100))
    bankAccountLevelTextR = Text("$"+str(playerBankAmount), [size[0]-50,150], size, (100,200,100))
    
    tooMuchMoneyTimer = 0
    while shop:
        pt = [0,0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    shopScroll = [0,-100]
                elif event.button == 5:
                    shopScroll = [0,100]
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pt = pygame.mouse.get_pos()
                elif event.button == 3:
                    shop = False
                    startup = True
                    for person in everyone:
                        person.kill()
                    bgColor = r,g,b = 250,110,110
                    
        bankAccountLevelTextL.kill()
        bankAccountLevelTextR.kill()
        bankAccountLevelTextL = Text("$"+str(playerBankAmount), [50,150], size, (100,200,100))
        bankAccountLevelTextR = Text("$"+str(playerBankAmount), [size[0]-50,150], size, (100,200,100))
        tooMuchMoney = Text("", [size[0]/2,size[1]/2], size, (250,70,70))
        
        attributes = ("#GAS TANK#","# PROFIT #","# COINS  #","# STARS  #","#BOOSTERS#")
        symbols = ('1','2','3','4','5','6')
        gasTankCosts = (500,650,900,1100,1500,3000)
        gasTankLevels = (25,40,50,60,70,(60*60))#starts at 15
        profitCosts = (650,1100,3000)
        profitLevels = (50,75,100)#starts at 25
        coinDensityCosts = (500,900,1500)
        coinDensities = (15,20,30)#starts at 10
        boosterDensityCosts = (1100,3000)
        boosterDensities = (10,15)#starts at 6
        for button in buttons:
            if button.isClicked(pt):
                print "don clicked: "+str(button), button.symbol, button.attribute
                if button.attribute == attributes[0]:
                    c=0
                    for symbol in symbols:
                        if button.symbol == symbol:
                            if playerBankAmount >= gasTankCosts[c]:
                                playerMaxFuelTime = gasTankLevels[c]
                                playerBankAmount += -gasTankCosts[c]
                                print playerMaxFuelTime
                            else:
                                tooMuchMoney = Text("That costs too much!!!", [size[0]/2,size[1]/2], size, (250,70,70))
                                tooMuchMoneyTimer = 0
                        c+=1
                if button.attribute == attributes[1]:
                    c=0
                    for symbol in symbols:
                        if button.symbol == symbol:
                            if playerBankAmount >= profitCosts[c]:
                                #player.profit = profitLevels[c]
                                playerBankAmount += - profitCosts[c]
                                #print playerProfit
                            else:
                                tooMuchMoney = Text("That costs too much!!!", [size[0]/2,size[1]/2], size, (250,70,70))
                                tooMuchMoneyTimer = 0
                        c+=1
                if button.attribute == attributes[2]:
                    c=0
                    for symbol in symbols:
                        if button.symbol == symbol:
                            if playerBankAmount >= coinDensityCosts[c]:
                                coinDensity = coinDensities[c]
                                playerBankAmount += - coinDensityCosts[c]
                                print coinDensity
                            else:
                                tooMuchMoney = Text("That costs too much!!!", [size[0]/2,size[1]/2], size, (250,70,70))
                                tooMuchMoneyTimer = 0
                        c+=1
                if button.attribute == attributes[4]:
                    c=0
                    for symbol in symbols:
                        if button.symbol == symbol:
                            if playerBankAmount >= boosterDensityCosts[c]:
                                boosterDensity = boosterDensities[c]
                                playerBankAmount += -boosterDensityCosts[c]
                                print boosterDensity
                            else:
                                tooMuchMoney = Text("That costs too much!!!", [size[0]/2,size[1]/2], size, (250,70,70))
                                tooMuchMoneyTimer = 0
                        c+=1
        
        
        tooMuchMoneyTimer += 1
        
        for textBox in textBoxes:
            if tooMuchMoneyTimer > 100:
                tooMuchMoney.kill()
                print "don killed a tooMuchMoney"
        all.update(size,
                shopScroll)
        shopScroll = [0,0]
            
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
    
    for person in everyone:
        person.kill()
    
    level = Level("Levels/Level1.layout", playerBankAmount, playerMaxFuelTime)

    player = level.player
    
    bgColor = r,g,b = 135, 206, 235
    
    startupCount = 0
    while startup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        
        #foward
        if startupCount < 245:
            player.previousTilt = player.tilt
            player.tilt = 5
            player.speed = [2,0]
            player.staticTilt()
            player.staticMove() 
            
        
        #tip down start scroll    
        elif startupCount >= 245 and startupCount < 295:
            player.previousTilt = player.tilt
            player.tilt = -40
            player.speed = [3,3]
            all.update(size,
                player.speed,
                player.didStaticMove)
            
        #foward at bottom    
        elif startupCount >= 295 and startupCount < 312:
            player.previousTilt = player.tilt
            player.tilt = 5
            player.speed = [4,0]
            all.update(size,
                player.speed,
                player.didStaticMove)
                
        # up 
        elif startupCount >= 312 and player.rect.center[1] > height/2:
            player.previousTilt = player.tilt
            player.tilt = 50
            player.speed = [2,-2]
            player.staticMove()
            all.update(size,
                player.speed,
                player.didStaticMove)
        
        # straight after launch        
        elif startupCount <= 458 :
            #raw_input("-->")
            player.previousTilt = player.tilt
            player.tilt = 0
            player.speed = [-1,0]
            player.staticMove()
            player.speed = [4,0]
            all.update(size,
                player.speed,
                player.didStaticMove)
                
        else:
            player.previousTilt = player.tilt
            player.tilt = 0
            player.speed = [4,0]
            all.update(size,
                player.speed,
                player.didStaticMove)
        
        if startupCount > 500:
            startup = False
                
        #raw_input("-->")
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        #print startupCount, player.rect.center, [width/2, height/2]
        startupCount += 1

    player.speed = [5,0]
    player.place([width/2, height/2])
    #print [width/2, height/2]
    
    start = time.time()
    
    while not startup and player.fuelLevel > 0: 
        now = time.time() -start
        #print "Loop start: ", now
        start = time.time()
        
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
        
        now = time.time() -start
        #print "Event handling: ", now
        start = time.time()
        
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
                    Cloud("Pictures/Blocks, and background/BadCloud.png",
                            [1500, y])                
                elif gamePiece == 11 or gamePiece ==12 or gamePiece == 13 or gamePiece == 14 or gamePiece == 15 or gamePiece == 16:
                    Booster(["Pictures/Game pieces/Booster1.png",
                                "Pictures/Game pieces/Booster2.png",
                                "Pictures/Game pieces/Booster3.png",
                                "Pictures/Game pieces/Booster2.png"], "^",
                            [1100, y])
        
        now = time.time() -start
        #print "spawning: ", now
        start = time.time()
        
        #for c in coins:
            #if cc == 0:
                #cc = c
            #elif cc not in coins:
                #cc = 0
            #else:
                #pass
                #print cc.rect.center, cc.virtPos
                
        
        playersHit_gamePieces = pygame.sprite.groupcollide(players, gamePieces, False, False)
        
        now = time.time() -start
        #print "collision grouping: ", now
        start = time.time()
        
        for p in playersHit_gamePieces:
            for piece in playersHit_gamePieces[p]:
                if p.collideBlock(piece):
                    pass
        
        now = time.time() -start
        #print "collision handled: ", now
        start = time.time()
                    
        if player.virtPos[1] >= 50000 - (player.virtPos[0] + 200):
            r,b,g = 250,110,110
                    
        for coin in coins:
            if coin.rect.center[1] > ground:
                coin.kill()
        for booster in boosters:
            if booster.rect.center[1] > ground:
                booster.kill()
        
        now = time.time() -start
        #print "kill objects: ", now
        start = time.time()
        
        all.update(size,
                player.speed,
                player.didStaticMove,
                player.fuelLevel)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
        
        now = time.time() -start
        #print "drawing: ", now
        start = time.time()
        #print ">>>>>>>>>>>>>>>>>>>>  FPS>>>>> ",clock.get_fps()
        
    while not startup and player.fuelLevel < 0 and player.rect.center[1] < 1100:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        if player.rect.center[1] > 700:
            print "refreshing"
            shop = True
            player.fuelLevel = player.maxFuelLevel
        
        player.speed = [3,2]
        player.staticMove()
        print player.bankAmount
        
        playerBankAmount = player.bankAmount
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
    
