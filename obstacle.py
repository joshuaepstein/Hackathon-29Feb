import pygame
class Obstacle:
    def __init__(self,x,y,texture,damage,speed,width):
        self.x=x #probably 800?
        self.y=y
        self.texture=texture 
        self.damage=damage # damage dealt to player on contact (total is 100)
        self.speed=speed # the speed that it moves to the left 
        self.image = pygame.image.load(self.texture)
        self.width=width
    def move(self):
        self.x-=self.speed
    def show(self,su):
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.width / self.image.get_height()), self.width))
        su.blit(self.image,(self.x,self.y))

    def createRect(self):
        return pygame.Rect(self.x,self.y,100,100)