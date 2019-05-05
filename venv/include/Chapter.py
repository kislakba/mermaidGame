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
score_msg = health_font.render("Score:", 1, pygame.Color("orange"))
score_msg_size = health_font.size("Score")
time_font = pygame.font.Font(None, 38)
time_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 46)
game_over_msg = game_over_font.render("Game Over", 1, pygame.Color("white"))
won_font = pygame.font.Font(None, 46)
won_msg = won_font.render("YOU WON!!!", 1, pygame.Color("white"))
time_msg = time_font.render("Time:", 1, pygame.Color("white"))
time_msg_size = time_font.size("Time")
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
        self.generateBubbleTimer = pTimer(2,self.generateBubble,screen)
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
        health_numb = health_numb_font.render(str(hp), 1, pygame.Color("red"))
        screen.blit(health_msg, (screen.get_width() - health_msg_size[0] - 60, 10))
        screen.blit(health_numb, (screen.get_width() - 45, 14))
    def drawScore(self,screen,score):
        score_numb = score_numb_font.render(str(score), 1, pygame.Color("orange"))
        screen.blit(score_msg, ((screen.get_width()/2) - score_msg_size[0] , 10))
        screen.blit(score_numb, ((screen.get_width()/2) +14, 14))

    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage, (self.backGroundImageX, 0))
        self.backGroundImageX = self.backGroundImageX - 1
        screen.blit(self.backGroundImage, (screen.get_width() + self.backGroundImageX, 0))
        if screen.get_width() == -self.backGroundImageX:
            self.backGroundImageX = 0

    def drawGameTime(self,screen,gameTime):
        game_time = time_font.render("Time:", 1, pygame.Color("red"))
        game_time_numb = time_numb_font.render(str(gameTime / 1000), 1, pygame.Color("green"))
        screen.blit(game_time, (30, 10))
        screen.blit(game_time_numb, (105, 14))

    def drawMermaid(self, screen, mposition):
        if self.mermaid.breath <= 0:
            pygame.event.post(self.mermaid.exposedEvent)
            self.mermaid.draw(screen, mposition)
            self.finish(screen)
        self.mermaid.draw(screen, mposition)

    def drawTargets(self, screen):
        for target in self.targets:
            if target.count %2 ==0:
                exposed = target.drawRight(screen)
                if type(target)==Bubble:
                    self.place=self.place+1
            if target.count %2 ==1:
                exposed = target.drawLeft(screen)
                self.place = self.place + 1

            if exposed:
                if type(target) == Bubble:
                    self.mermaid.breath += 10

                self.targets.remove(target)
                pygame.event.post(target.ExposedEvent)
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
                        if target.rectangle.colliderect(bullet.rectangle):
                            print("hithit")
                            target.hit()
                            self.mermaid.bullets.remove(bullet)

    def draw(self, screen, mposition, gt):
        self.drawBackGround(screen)
        self.drawMermaid(screen, mposition)
        self.drawTargets(screen)
        self.drawHp(screen, self.mermaid.breath)
        self.drawScore(screen,self.mermaid.score)
        self.drawGameTime(screen, gt)