#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
class Bullet():
    def __init__(self,plane):
        self.x=0
        self.y=0
        self.mx=0 #x haraket yönü
        self.my=0 #x haraket yönü

        self.rectangle=pygame.rect.Rect(plane.rectange[0] + plane.rectange[2], plane.rectange[1] + int(plane.rectange[3] / 2), int(plane.rectange[2] / 5), int(plane.rectange[3] / 5))
        self.image=pygame.transform.scale(pygame.image.load("images/hook4x.png"),(self.rectangle[2],self.rectangle[3]))
    def draw(self,screen):
        self.rectangle[0]=self.rectangle[0]+self.mx*3
        self.rectangle[1]=self.rectangle[1]+self.my*3
        #self.rectange.clamp_ip(screen.get_rect())
        ##mermi objesini ekran karesi içinden çıkarsa silinir
        ##bunu planeden kontrol edeceğiz.
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
        mx=float(mposition[0]-350)
        my=float(mposition[1]-250)
        nbullet.mx=float(mx/my)
        nbullet.my=float(my/mx)
        if my<0 and mx<0:
            nbullet.my=nbullet.my * -1
            nbullet.mx=nbullet.mx *-1
        elif mx<0:
            nbullet.my=nbullet.my*-1
        elif my<0:
            nbullet.mx=nbullet.my*-1

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

