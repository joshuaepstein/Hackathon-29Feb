import pygame
import random

class Collectable:

    static_textures = [
        pygame.image.load("assets/0.png"),
        pygame.image.load("assets/1.png"),
    ]

    def __init__(self):
        self.texture_location = random.choice(self.static_textures)
        self.points = random.randint(1, 4)
        self.x = 800
        self.y = random.randint(1,800)

    def getTexture(self):
        return self.texture_location
    
    def getPoints(self):
        return self.points
    
    def draw(self, screen, frames):
        self.x -= 1
        screen.blit(self.texture_location, (self.x, self.y))

    def getRect(self):
        return pygame.Rect(self.x, self.y, 20, 20)
    
    def collide(self, player):
        if self.getRect().colliderect(player.getRect()):
            return True
        return False