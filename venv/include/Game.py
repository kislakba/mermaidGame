import pygame
import sys
import math
import random
from Chapter import ChapterOne
gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False
clock = pygame.time.Clock()
backGroundImage=pygame.image.load("images/BG.png")
backGroundImage= pygame.transform.scale(backGroundImage, (gameDisplay.get_width(), gameDisplay.get_height()))
chapter = ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent = pygame.event.Event(pygame.USEREVENT, attrl='endEvent')
end = False
while not crashed:
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            chapter.mermaid.fire(mouse_position)
    gameDisplay.blit(backGroundImage,(0,0))
    chapter.mermaid.draw(gameDisplay,mouse_position)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
