import pygame
pygame.init()
import random
import math


FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((400, 300), pygame.FULLSCREEN)
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS

def displayMessage(msg,loc,colour=(0,0,0),size=15):
    font = pygame.font.SysFont('Times New Roman', size)
    screen.blit(font.render(msg,True,colour),loc)

## Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y1 > (10):
        y1 -= speed
    if keys[pygame.K_s] and y1 < (270):
        y1 += speed
    if keys[pygame.K_UP] and y2 > (10):
        y2 -= speed
    if keys[pygame.K_DOWN] and y2 < (270):
        y2 += speed
    
    pygame.display.flip()       


pygame.quit()
quit()