import pygame
import sys
import math
import random
from threading import Timer
from Shark import Shark
from JellyFish import JellyFish
from LittleFish import LittleFish
from Mermaid import Mermaid
from Bullet import Bullet
from pTimer import pTimer

class ChapterOne():
    def __init__(self, screen):
        self.name = "Let's Start"
        self.mermaid = Mermaid(screen)
        self.targets = []
        self.backGroundImage = pygame.transform.scale(pygame.image.load("images/BG.png"),
                                                      (screen.get_width(), screen.get_height()))
        self.backGroundImageX = 0
        self.backGroundImageY = 0
        self.place = 0
        self.screen = screen
        self.pgenerateTargetTimer = pTimer(7, self.generateTarget, screen)
        self.pgenerateTargetTimer2 = pTimer(5, self.generateJelly, screen)
        self.pgenerateTargetTimer3 = pTimer(3, self.generateLittle, screen)
        self.finishEvent = pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')

    def start(self, screen):
        self.pgenerateTargetTimer.start()
        self.pgenerateTargetTimer2.start()
        self.pgenerateTargetTimer3.start()

    def finish(self, screen):
        self.pgenerateTargetTimer.stop()
        self.pgenerateTargetTimer2.stop()
        self.pgenerateTargetTimer3.stop()
        pygame.event.post(self.finishEvent)

    def generateTarget(self, arguments):
        newTarget = Shark(arguments[0],self.place)
        self.targets.append(newTarget)
    def generateLittle(self, arguments):
        newTarget = LittleFish(arguments[0],self.place)
        self.targets.append(newTarget)
    def generateJelly(self, arguments):
        newTarget = JellyFish(arguments[0],self.place)
        self.targets.append(newTarget)

    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage, (self.backGroundImageX, 0))
        self.backGroundImageX = self.backGroundImageX - 1
        screen.blit(self.backGroundImage, (screen.get_width() + self.backGroundImageX, 0))
        if screen.get_width() == -self.backGroundImageX:
            self.backGroundImageX = 0

    def drawPlane(self, screen, mposition):
        self.mermaid.draw(screen, mposition)

    def drawTargets(self, screen):
        for target in self.targets:
            if target.count %2 ==0:
                exposed = target.drawRight(screen)
                self.place=self.place+1
            if target.count %2 ==1:
                exposed = target.drawLeft(screen)
                self.place = self.place + 1
            if exposed:
                self.targets.remove(target)
                if self.mermaid.exposed:
                    pygame.event.post(self.mermaid.exposedEvent)
                    self.finish(screen)

            else:
                if target.rectangle.colliderect(self.mermaid.rectangle):
                    if not target.exposed:
                        target.expose()
                        self.mermaid.expose()

                else:
                    for bullet in self.mermaid.bullets:
                        # eğer eşleşme varsa
                        if target.rectangle.colliderect(bullet.rectangle):
                            print("hithit")
                            # target hit almış demektir.
                            target.hit()
                            # mermi kaybolmalı
                            self.mermaid.bullets.remove(bullet)

    def draw(self, screen, mposition):
        self.drawBackGround(screen)
        self.drawPlane(screen, mposition)
        self.drawTargets(screen)
