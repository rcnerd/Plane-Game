import sys, pygame, math, random
from Ball import *
from Wall import *
from Level import *
from PlayerBall import *
pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

balls = pygame.sprite.Group()
players = pygame.sprite.Group()
boundries = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Ball.containers = (balls, all)
Wall.containers = (boundries, all)
PlayerBall.containers = (players, all)

level = Level("level1.lvl")

player = level.player

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            elif event.key == pygame.K_DOWN:
                player.go("down")
            elif event.key == pygame.K_LEFT:
                player.go("left")
            elif event.key == pygame.K_RIGHT:
                player.go("right")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            elif event.key == pygame.K_DOWN:
                player.go("stop down")
            elif event.key == pygame.K_LEFT:
                player.go("stop left")
            elif event.key == pygame.K_RIGHT:
                player.go("stop right")
    
    all.update(size)
    
    playersHitBalls = pygame.sprite.groupcollide(players, balls, False, True)
    playersHitBoundries = pygame.sprite.groupcollide(players, boundries, False, False)
    ballsHitBoundries = pygame.sprite.groupcollide(balls, boundries, False, False)
    ballsHitBalls = pygame.sprite.groupcollide(balls, balls, False, False)
    
    for p in playersHitBoundries:
        for boundry in playersHitBoundries[p]:
            p.collideBoundry(boundry)
    
    for ball in ballsHitBoundries:
        for boundry in ballsHitBoundries[ball]:
            ball.collideBoundry(boundry)
    
    for ball1 in ballsHitBalls:
        for ball2 in ballsHitBalls[ball1]:
            ball1.collideBall(ball2)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)










