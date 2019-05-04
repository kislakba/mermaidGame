import pygame
import sys
import math
import random
from Bullet import Bullet
class Mermaid():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.rectangle=[self.width/2-50,self.height/2-50,int(self.width/5),int(self.height/5)]
        self.bullets = []
        self.imageOrder = 0
        self.breath = 140
        self.swimImages = [pygame.transform.scale(pygame.image.load("images/sb1.png"),
                                                  (self.rectangle[2], self.rectangle[3])),
                           pygame.transform.scale(pygame.image.load("images/sb2.png"),
                                                 (self.rectangle[2], self.rectangle[3])),
                           pygame.transform.scale(pygame.image.load("images/sb3.png"),
                                                 (self.rectangle[2], self.rectangle[3])),
                           pygame.transform.scale(pygame.image.load("images/sb4.png"),
                                                 (self.rectangle[2], self.rectangle[3]))]
        self.exposedImage = pygame.transform.scale(pygame.image.load("images/sbd.png"),
                                                   (self.rectangle[2], self.rectangle[3]))
        self.exposed = False
        self.exposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='planeExposedEvent')
    def decrease(self,screen):
        self.breath -= 14

    def draw(self, screen, mposition):
        if self.exposed:
            screen.blit(self.exposedImage,self.rectangle)
            return True
        self.imageOrder = self.imageOrder % 4 + 1
        self.image = pygame.image.load("images/sb" + str(self.imageOrder) + ".png")
        self.image = pygame.transform.scale(self.image, (self.rectangle[2], self.rectangle[3]))
        angle = math.atan2((self.rectangle[1] + int(self.rectangle[3] / 2) - mposition[1]),
                           (mposition[0] - self.rectangle[0]))
        self.image = pygame.transform.rotate(self.image, math.degrees(angle))
        screen.blit(self.image, self.rectangle)
        for bullet in self.bullets:
            bullet.draw(screen)
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet)

    def fire(self, mposition):
        nbullet = Bullet(self)
        mx = float(mposition[0] - self.width/2)
        my=float(mposition[1]-self.height/2)
        angle = math.atan2(my, mx)
        nbullet.mx = float(math.cos(angle)) * 10
        nbullet.my = float(math.sin(angle)) * 10
        print(nbullet.mx)
        print(nbullet.my)
        nbullet.image = pygame.transform.rotate(nbullet.image, -math.degrees(angle))
        self.bullets.append(nbullet)

    def expose(self):
        self.exposed = True
    def noBreathe(self):
        pass
