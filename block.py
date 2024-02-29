import pygame


class Block:
    # The block class should be setup for collision so it should store a location and a size
    # The location should be a tuple of x and y
    # The size should be a tuple of width and height

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def getTexture(self):
        return "block.png"

    def draw(self, screen):
        image = pygame.image.load(self.getTexture())
        screen.blit(image, (self.x, self.y))
    
    def collide(self, player):
        if player.x + player.width > self.x and player.x < self.x + self.width and player.y + player.height > self.y and player.y < self.y + self.height:
            return True
        return False
    
    def move(self, speed):
        self.x -= speed
