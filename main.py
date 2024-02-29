import pygame
pygame.init()
frames = 0
import random
import math
from player import Player
from worldutils import WorldUtils
from firewall import Firewall
from error import Error
from healthbar import Healthbar
from collectable import Collectable


FPS = 60

# Define Colours 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Malware Run")
clock = pygame.time.Clock()     ## For syncing the FPS

def displayMessage(msg,loc,colour=(0,0,0),size=15):
    font = pygame.font.SysFont('Arial', size)
    screen.blit(font.render(msg,True,colour),loc)

## Game loop
running = True

block_image = pygame.Surface((50, 50))
block_image.fill((255, 0, 0))
player_image = pygame.Surface((50, 50))
player_image.fill((0, 255, 0))
world = WorldUtils(screen, block_image, player_image, speed=5, width=800, height=800)

h=Healthbar()

player=Player()
enemies=[]
collectables=[]
points = 0
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK) # change to background image!!
    world.draw(frames=frames)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move_up()
        pass
    if keys[pygame.K_DOWN]:
        player.move_down()
        pass
    if (random.randint(1,200) == 1 and player.health>0):
        enemies.append(random.choice((Firewall(),Error())))
    if (random.randint(1, 300) == 1 and player.health > 0):
        collectables.append(Collectable())
    
    if player.health > 0:
        for i in enemies:
            i.move()
            i.show(su=screen)
            if i.x<10:
                enemies.pop(enemies.index(i))
            if i.createRect().colliderect(player.getRect()):
                player.health-=i.damage
                enemies.pop(enemies.index(i))
        for collectable in collectables:
            collectable.draw(screen=screen, frames=frames)
            # if collectable.createRect().colliderect(player):
            #     points += collectable.getPoints()
            #     collectables.pop(collectables.index(collectable)) 
        player.show(screen,frames)
        h.show(screen,player.health)

    if player.health<=0:
        enemies=[]
        screen.fill(BLACK)
        displayMessage("YOU DIED!!!!",(100,100),colour=(WHITE),size=50)
        
    pygame.display.flip()       
    frames+=1

pygame.quit()
quit()