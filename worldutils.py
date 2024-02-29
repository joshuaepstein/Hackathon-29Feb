import pygame
import random

class WorldUtils:
    blocks = []
    background = pygame.image.load("assets/background.JPG")

    def __init__(self, screen, block, player, speed, width, height):
        self.screen = screen
        self.player = player
        self.speed = speed
        self.width = width
        self.height = height

    def draw(self, frames):
        for block_pos in self.blocks:
            self.screen.blit(self.block, block_pos)

        self.drawBackground(frames=frames)
        
    def drawBackground(self, frames=0):
        # imageWidth = self.background.get_width()
        # self.background = pygame.transform.scale(self.background, (800, 800))
        # x = 800-(frames % imageWidth)
        # self.screen.blit(self.background, (x - imageWidth, 0))
        # if x < self.width:
        #     self.screen.blit(self.background, (x, 0))
        # ^ Using code above, without changing how it works, double the speed so it moves the background faster
        imageWidth = self.background.get_width()
        self.background = pygame.transform.scale(self.background, (800, 800))
        x = 800-(frames*5 % imageWidth)
        self.screen.blit(self.background, (x - imageWidth, 0))
        if x < self.width:
            self.screen.blit(self.background, (x, 0))
