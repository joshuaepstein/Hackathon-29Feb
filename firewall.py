from obstacle import Obstacle
import random
class Firewall(Obstacle):
    def __init__(self):
        Obstacle.__init__(self=self,x=800,y=random.randint(1,800),texture="assets/firewall.JPG",damage=20,speed=10,width=100)
    