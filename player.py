import pygame
keys = pygame.key.get_pressed()
class Player:
    images = []
    vimages=[]
    def __init__(self,im):
        self.x=120
        self.y=360
        self.speed=8
        self.jump=False
        self.health = 100
        self.im = im
        imageLocations = ["assets/player1.png","assets/player2.png","assets/player3.png","assets/player4.png",
                "assets/player5.png","assets/player6.png","assets/player7.png","assets/player8.png"]
        for i in range(8):
            z=pygame.image.load(imageLocations[i])
            x=pygame.transform.scale(z,(z.get_width()//3,z.get_height()//3))
            self.images.append(x)

        vimageLocations = ["assets/v1.png","assets/v2.png","assets/v3.png","assets/v4.png"]
        for i in range(4):
            z=pygame.image.load(vimageLocations[i])
            x=pygame.transform.scale(z,(z.get_width()//3,z.get_height()//3))
            self.vimages.append(x)

    def getRect(self):
        return pygame.Rect(self.x, self.y, 50, 50)
    
    def move_up(self):
        if self.y>25:
            self.y-=self.speed
    def move_down(self):
        if self.y<600:
            self.y+=self.speed
    
    def show(self,sc,fr):
        sc.blit(self.images[int(fr/4) % 8],(self.x,self.y))
        sc.blit(self.vimages[int(fr/4) % 4],(0,400))

    def createRect(self):
        return pygame.Rect(self.x,self.y,242,242)

        