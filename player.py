import pygame
keys = pygame.key.get_pressed()
class Player:
    images = []
    
    def __init__(self):
        self.x=50
        self.y=360
        self.speed=8
        self.jump=False
        self.health = 100
        imageLocations = ["assets/player1.png","assets/player2.png","assets/player3.png","assets/player4.png",
                "assets/player5.png","assets/player6.png","assets/player7.png","assets/player8.png"]
        for i in range(8):
            self.images.append(pygame.image.load(imageLocations[i]))

    def getRect(self):
        return pygame.Rect(self.x, self.y, 50, 50)
    
    def move_up(self):
        if self.y>15:
            self.y-=self.speed
    def move_down(self):
        if self.y<512:
            self.y+=self.speed
    
    def show(self,sc,fr):
        sc.blit(self.images[int(fr/4) % 8],(self.x,self.y))

    def createRect(self):
        return pygame.Rect(self.x,self.y,50,50)