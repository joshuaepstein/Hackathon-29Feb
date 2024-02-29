from obstacle import Obstacle
import random
class Error(Obstacle):
    def __init__(self):
        Obstacle.__init__(self=self,x=800,y=random.randint(20,512),texture="assets/error_block.JPG",damage=10,speed=15,width=50)
        