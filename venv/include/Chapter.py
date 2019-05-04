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
from Bubble import Bubble
from pTimer import pTimer
pygame.font.init()
health_font = pygame.font.Font(None, 38)
health_numb_font = pygame.font.Font(None, 28)
health_msg = health_font.render("Hp:", 1, pygame.Color("Purple"))
health_msg_size = health_font.size("Hp")
score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 46)
play_again_font = score_numb_font
score_msg = score_font.render("Time:", 1, pygame.Color("white"))
score_msg_size = score_font.size("Time")
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
        self.decreasingTimer = pTimer(3,self.mermaid.decrease,screen)
        self.finishEvent = pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')
        self.generateBubbleTimer = pTimer(3,self.generateBubble,screen) #ben vurunca bubble expose olunca hp yükseltilecek.
    def start(self, screen):
        self.pgenerateTargetTimer.start()
        self.pgenerateTargetTimer2.start()
        self.pgenerateTargetTimer3.start()
        self.generateBubbleTimer.start()
        self.decreasingTimer.start()

    def finish(self, screen):
        self.pgenerateTargetTimer.stop()
        self.generateBubbleTimer.stop()
        self.pgenerateTargetTimer2.stop()
        self.pgenerateTargetTimer3.stop()
        self.decreasingTimer.stop()
        pygame.event.post(self.finishEvent)
    def generateBubble(self,arguments):
        newTarget = Bubble(arguments[0])
        self.targets.append(newTarget)
    def generateTarget(self, arguments):
        newTarget = Shark(arguments[0],self.place)
        self.targets.append(newTarget)
    def generateLittle(self, arguments):
        newTarget = LittleFish(arguments[0],self.place)
        self.targets.append(newTarget)
    def generateJelly(self, arguments):
        newTarget = JellyFish(arguments[0],self.place)
        self.targets.append(newTarget)
    def drawHp(self,screen,hp):
        score_numb = health_numb_font.render(str(hp), 1, pygame.Color("red"))
        screen.blit(health_msg, (screen.get_width() - health_msg_size[0] - 60, 10))
        screen.blit(score_numb, (screen.get_width() - 45, 14))

    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage, (self.backGroundImageX, 0))
        self.backGroundImageX = self.backGroundImageX - 1
        screen.blit(self.backGroundImage, (screen.get_width() + self.backGroundImageX, 0))
        if screen.get_width() == -self.backGroundImageX:
            self.backGroundImageX = 0

    def drawGameTime(self,screen,gameTime):
        game_time = score_font.render("Time:", 1, pygame.Color("red"))
        game_time_numb = score_numb_font.render(str(gameTime / 1000), 1, pygame.Color("green"))
        screen.blit(game_time, (30, 10))
        screen.blit(game_time_numb, (105, 14))

    def drawMermaid(self, screen, mposition):
        self.mermaid.draw(screen, mposition)

    def drawTargets(self, screen):
        for target in self.targets:
            if target.count %2 ==0:
                exposed = target.drawRight(screen)
                if type(target)==Bubble:
                    print("balon")
                self.place=self.place+1
            if target.count %2 ==1:
                exposed = target.drawLeft(screen)
                self.place = self.place + 1
            if exposed:
                if type(target) == Bubble:
                    self.mermaid.breath += 10

                self.targets.remove(target)
                if self.mermaid.exposed:
                    pygame.event.post(self.mermaid.exposedEvent)
                    self.finish(screen)

            else:
                if target.rectangle.colliderect(self.mermaid.rectangle) and type(target)!=Bubble:
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

    def draw(self, screen, mposition, gt):
        self.drawBackGround(screen)
        self.drawMermaid(screen, mposition)
        self.drawTargets(screen)
        self.drawHp(screen, self.mermaid.breath)
        self.drawGameTime(screen, gt)