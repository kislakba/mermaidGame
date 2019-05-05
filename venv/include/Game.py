import pygame
import sys
import math
import random
import Chapter
from Menu import Menu
from Chapter import ChapterOne
from LittleFish import LittleFish
from JellyFish import JellyFish
from Shark import Shark
pygame.init()
gameDisplay_width=1000
gameDisplay_height=750
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')
crashed = False
clock = pygame.time.Clock()
backGroundImage=pygame.image.load("images/BG.png")
backGroundImage= pygame.transform.scale(backGroundImage, (gameDisplay.get_width(), gameDisplay.get_height()))
chapter = ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent = pygame.event.Event(pygame.USEREVENT, attrl='endEvent')
menu=Menu(gameDisplay.get_rect())
end = False
start = pygame.time.get_ticks()
while not crashed:
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                chapter.pgenerateTargetTimer.pause(True)
                crashed = menu.runMenu(gameDisplay)
                chapter.pgenerateTargetTimer.pause(False)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            chapter.mermaid.fire(mouse_position)

        elif event == chapter.finishEvent:
            print(event)
            gameDisplay.blit(Chapter.game_over_msg, (gameDisplay_width/2-40,gameDisplay_height/2))
            end=True
        elif event == LittleFish.ExposedEvent:
            chapter.mermaid.score +=5
        elif event == JellyFish.ExposedEvent:
            chapter.mermaid.score +=7
        elif event == Shark.ExposedEvent:
            chapter.mermaid.score +=12

    if not end:
        gameTime = 30000-pygame.time.get_ticks()- start
        chapter.draw(gameDisplay,mouse_position,gameTime)
        if gameTime <= 0:
            if chapter.mermaid.score>40:
                gameDisplay.blit(Chapter.won_msg,(gameDisplay_width/2-40,gameDisplay_height/2))
                end = True
            else:
                gameDisplay.blit(Chapter.game_over_msg, (gameDisplay_width / 2 - 40, gameDisplay_height / 2))
                end = True


    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
