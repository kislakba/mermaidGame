import pygame
import sys
import random
class Shark():
    ExposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='SharkExposed')
    def __init__(self, screen, count):
        self.x = 0
        self.count = count
        self.y = 0
        self.mx = 1
        self.my = 0
        self.life = 150
        width = screen.get_width()
        height = screen.get_height()
        self.y = random.randint(10, height - int(height / 5))
        self.rectangle = pygame.rect.Rect(width + int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 12),
                                          int(height / 6))

        self.flyImageOrder = 0
        self.flyImages = []
        self.flyImagesLeft=[]
        for i in range(0, 5):
            self.flyImages.append(
                pygame.transform.scale(pygame.image.load("images/sha" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))
        for i in range(0, 5):
            self.flyImagesLeft.append(
                pygame.transform.scale(pygame.image.load("images/shark" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))
        self.exposed = False

    def drawRight(self, screen):
        if self.exposed == False:
            self.flyImageOrder = (self.flyImageOrder + 1) % 5
            self.rectangle[0] = self.rectangle[0] - self.mx * 2
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.rectangle[0] - int(self.flyImages[self.flyImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])
        else:
            return True
    def drawLeft(self, screen):
        if self.rectangle[0]>1000:
            self.rectangle[0]=-25
        if self.exposed == False:
            self.flyImageOrder = (self.flyImageOrder + 1) % 5
            self.rectangle[0] = self.rectangle[0] + self.mx * 2
            screen.blit(self.flyImagesLeft[self.flyImageOrder],
                        [self.rectangle[0] - int(self.flyImagesLeft[self.flyImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.flyImagesLeft[self.flyImageOrder].get_height() / 2)])
        else:
            return True
    def hit(self):
        self.life = self.life - 50
        if self.life <= 0:
            self.expose()

    def expose(self):
        self.life = 0
        self.exposed = True

