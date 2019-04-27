#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
from builtins import print

import pygame
import sys
import math
import random
class TargetOne():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #y haraket yönü
        self.life=100
        width=screen.get_width()
        height=screen.get_height()
        self.y=random.randint(10,height-int(height/5))
        self.rectangle=pygame.rect.Rect(width+int(width/20)/2,self.y+int(height/10)/2,int(width/20),int(height/10))

        self.flyImageOrder=0
        self.flyImages=[]
        for i in range(1,11):
            self.flyImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Idle ("+str(i)+").png"),(self.rectangle[2],self.rectangle[3])))

        self.explosionImageOrder=-1
        self.explosionImages=[]
        for i in range(1,10):
            self.explosionImages.append(pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_1_Expo ("+str(i)+").png"),(self.rectangle[2]*4,self.rectangle[2]*4)))

    def draw(self,screen):
        if self.explosionImageOrder==-1:
            self.flyImageOrder=(self.flyImageOrder+1)%10
            self.rectangle[0]=self.rectangle[0]-self.mx*2
            #self.rectangle[1]=self.rectangle[1]-self.my*2
            #self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.flyImages[self.flyImageOrder], [self.rectangle[0]-int(self.flyImages[self.flyImageOrder].get_width()/2),self.rectangle[1]-int(self.flyImages[self.flyImageOrder].get_height()/2)])
        else:
            self.explosionImageOrder=(self.explosionImageOrder+1)%9
            #self.rectangle[0]=self.rectangle[0]-self.mx*2
            #self.rectangle[1]=self.rectangle[1]-self.my*2
            self.rectangle.centerx= self.rectangle.centerx-self.mx*2

            screen.blit(self.explosionImages[self.explosionImageOrder], [self.rectangle[0]-int(self.explosionImages[self.explosionImageOrder].get_width()/2),self.rectangle[1]-int(self.explosionImages[self.explosionImageOrder].get_height()/2)])
            if self.explosionImageOrder==8:
                self.explosionImageOrder=-1

    def explosion(self):
        if self.life<=0:
            self.explosionImageOrder=0

class Bullet():
    def __init__(self,plane):
        self.x=0
        self.y=0
        self.mx=0.0 #x haraket yönü
        self.my=0.0 #y haraket yönü
        self.rectangle=pygame.rect.Rect(plane.rectange[0] + plane.rectange[2], plane.rectange[1] + int(plane.rectange[3] / 2), int(plane.rectange[2] / 5), int(plane.rectange[3] / 5))
        self.image=pygame.transform.scale(pygame.image.load("images/hook4x.png"),(self.rectangle[2],self.rectangle[3]))
    def draw(self,screen):
        self.rectangle[0]=self.rectangle[0]+self.mx
        self.rectangle[1]=self.rectangle[1]+self.my
        screen.blit(self.image, self.rectangle)
class Plane():
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.imageOrder=0
        width=screen.get_width()
        height=screen.get_height()
        self.rectange=[width/2-50,height/2-50,int(width/5),int(height/5)]
        self.bullets=[]
    def draw(self,screen,mposition):
        self.imageOrder=self.imageOrder%4+1
        self.image=pygame.image.load("images/sb"+str(self.imageOrder)+".png")
        self.image= pygame.transform.scale(self.image, (self.rectange[2],self.rectange[3]))
        angle = math.atan2((self.rectange[1]+int(self.rectange[3]/2) - mposition[1]), (mposition[0] - self.rectange[0]))
        self.image = pygame.transform.rotate(self.image, math.degrees(angle))
        screen.blit(self.image, self.rectange)
        for bullet in self.bullets:
            bullet.draw(screen)
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet)
    def fire(self,mposition):
        nbullet=Bullet(self)
        mx=float(mposition[0]-375)
        my=float(mposition[1]-275)
        angle =math.atan2(my,mx)
        nbullet.mx=float(math.cos(angle))*2
        nbullet.my=float(math.sin(angle))*2

        print(nbullet.mx)
        print(nbullet.my)
        nbullet.image = pygame.transform.rotate(nbullet.image, -math.degrees(angle))


        self.bullets.append(nbullet)
pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

white = (255, 255,255)

clock = pygame.time.Clock()
backGroundImage=pygame.image.load("images/BG.png")
backGroundImage= pygame.transform.scale(backGroundImage, (gameDisplay.get_width(), gameDisplay.get_height()))

 #ekranı her framede tekrar çizdiriyoruz
gamePlane=Plane(gameDisplay)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            gamePlane.fire(pygame.mouse.get_pos())
    gameDisplay.blit(backGroundImage,(0,0))
    mouse_position = pygame.mouse.get_pos()
    gamePlane.draw(gameDisplay,mouse_position)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

