import pygame
class Healthbar:
    def __init__(self):
        self.health=100
    def show(self,su,health):
        pygame.draw.rect(su,(100,100,100),(0,0,800,20))
        pygame.draw.rect(su,(255,0,0),(0,0,8*health,20))
        
    