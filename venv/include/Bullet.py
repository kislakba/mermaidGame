import pygame
import sys
import math
import random
class Bullet():
    def __init__(self,plane):
        self.x=0
        self.y=0
        self.mx=0.0 #x haraket yönü
        self.my=0.0 #y haraket yönü
        self.rectangle=pygame.rect.Rect(plane.rectangle[0] + plane.rectangle[2], plane.rectangle[1] + int(plane.rectangle[3] / 2), int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))
        self.image=pygame.transform.scale(pygame.image.load("images/hook4x.png"),(self.rectangle[2],self.rectangle[3]))
    def draw(self,screen):
        self.rectangle[0]=self.rectangle[0]+self.mx
        self.rectangle[1]=self.rectangle[1]+self.my
        screen.blit(self.image, self.rectangle)