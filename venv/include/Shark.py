import pygame
import sys
import random
class Shark():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx = 1  # x haraket yönü
        self.my = 0  # y haraket yönü
        self.life = 150
        width = screen.get_width()
        height = screen.get_height()
        self.y = random.randint(10, height - int(height / 5))
        self.rectangle = pygame.rect.Rect(width + int(width / 20) / 2, self.y + int(height / 10) / 2, int(width / 20),
                                          int(height / 10))

        self.flyImageOrder = 0
        self.flyImages = []
        for i in range(1, 5):
            self.flyImages.append(
                pygame.transform.scale(pygame.image.load("images/sha" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))
        self.exposed = False

    def draw(self, screen):
            self.flyImageOrder = (self.flyImageOrder + 1) % 10
            self.rectangle[0] = self.rectangle[0] - self.mx * 2
            # self.rectangle[1]=self.rectangle[1]-self.my*2
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.rectangle[0] - int(self.flyImages[self.flyImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2)])
    def hit(self):
        self.life = self.life - 50
        if self.life <= 0:
            self.expose()

    def expose(self):
        self.life = 0
        self.exposed = True
