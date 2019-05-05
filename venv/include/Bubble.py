import pygame
import sys
import random
class Bubble():
    ExposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='itsNotimportantTarget')
    def __init__(self, screen, count=0):
        self.x = 0
        self.count = count
        self.y = 0
        self.mx = 0
        self.my = 1
        self.life = 50
        width = screen.get_width()
        height = screen.get_height()
        self.y = width+(width/10)
        self.x = random.randint(10, width + int(width / 5))
        self.rectangle = pygame.rect.Rect(self.x, self.y + int(height / 10) / 2, int(width / 30),
                                          int(height / 20))
        self.flyImage = pygame.transform.scale(pygame.image.load("images/baloncuk.png"),(self.rectangle[2],self.rectangle[3]))
        self.exposed = False

    def drawRight(self, screen):
        if self.exposed == False:
            self.rectangle[1]=self.rectangle[1]-self.my*2
            screen.blit(self.flyImage,
                        [self.rectangle[0] - int(self.flyImage.get_width() / 2),
                         self.rectangle[1] - int(self.flyImage.get_height() / 2)])
        else:
            return True
    def hit(self):
        self.life = self.life - 50
        if self.life <= 0:
            print("ölllll")
            self.expose()

    def expose(self):
        self.life = 0
        self.exposed = True

