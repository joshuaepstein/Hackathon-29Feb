import pygame
import random

class Collectable:
    # pygame.transform.scale(self.image, (int(self.image.get_width() * self.width / self.image.get_height()), self.width))
    
    def __init__(self):
        zero=pygame.image.load("assets/0.png")
        zero=pygame.transform.scale(zero,(zero.get_width()*5,zero.get_height()*5))
        one=pygame.image.load("assets/1.png")
        one=pygame.transform.scale(one,(one.get_width()*5,one.get_height()*5))
        earring=pygame.image.load("assets/ringg.png")
        earring=pygame.transform.scale(earring,(int(earring.get_width()/5),int(earring.get_height()/5)))

        textures=[zero,one,earring]
        self.texture_location = random.choice(textures) 
        self.points = random.randint(1, 4)
        self.x = 800
        self.y = random.randint(20,512)

    def getTexture(self):
        return self.texture_location
    
    def getPoints(self):
        return self.points
    
    def draw(self, screen, frames):
        self.x -= 15
        screen.blit(self.texture_location, (self.x, self.y))

    def getRect(self):
        return pygame.Rect(self.x, self.y, 100, 100)
    
    def collide(self, player):
        if self.getRect().colliderect(player.getRect()):
            return True
        return False