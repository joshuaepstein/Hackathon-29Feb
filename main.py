import pygame
pygame.init()
frames = 0
import random
import time
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
keys = pygame.key.get_pressed()

def displayMessage(msg,loc,colour=(0,0,0),size=15):
    font = pygame.font.SysFont('Arial', size)
    screen.blit(font.render(msg,True,colour),loc)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    introtext=[
    "Due to an unfortunate twist of fate, the esteemed head of Computer",
    "Science, Mr Waring, has somehow got himself stuck inside",
    "his own computer!!! Even worse, he is now being attacked",
    "by a computer virus!!! Help him collect 1s, 0s, and stray",
    "confiscated hoop earrings, while avoiding firewalls and error messages!!",
    "Press the X in the top right to continue..."
    ]
    for i in range(len(introtext)):
        displayMessage(introtext[i],(10,i*50+100),colour=(WHITE),size=30)
    pygame.display.flip() 
## Game loop
running = True

block_image = pygame.Surface((50, 50))
block_image.fill((255, 0, 0))
player_image = pygame.Surface((800, 800))
world = WorldUtils(screen, block_image, player_image, speed=5, width=800, height=800)

h=Healthbar()

player=Player(player_image)
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
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()
    if (random.randint(1,100) == 1 and player.health>0):
        enemies.append(random.choice((Firewall(),Error(),Error())))
    if (random.randint(1,100) == 1 and player.health > 0):
        collectables.append(Collectable())
    
    if player.health > 0:
        for i in enemies:
            i.move()
            i.show(su=screen)
            if i.x<0:
                enemies.pop(enemies.index(i))
            elif i.createRect().colliderect(player.getRect()):
                player.health-=i.damage
                enemies.pop(enemies.index(i))
                print("hurt!!!!")


        for j in collectables:
            j.draw(screen=screen, frames=frames)
            if j.x<0:
                collectables.pop(collectables.index(j))
            elif j.getRect().colliderect(player.getRect()):
                points += j.getPoints()
                collectables.pop(collectables.index(j))
                print("collected!!!!")
            
        player.show(screen,frames)
        h.show(screen,player.health)
        pygame.draw.rect(screen,BLUE,(700,20,100,50))
        displayMessage("Pts: "+str(points),(720,28),size=30,colour=WHITE)

    if player.health<=0:
        enemies=[]
        screen.fill(BLACK)
        displayMessage("Mr waring was tragically eaten by the virus",(20,400),colour=(WHITE),size=50)
        displayMessage("score: "+str(points),(20,500),colour=(WHITE),size=50)
        
    pygame.display.flip()       
    frames+=1

pygame.quit()
quit()