import pygame

class Bullet():
    def __init__(self,mermaid):
        self.x=0
        self.y=0
        self.mx=0
        self.my=0

        self.rectangle = pygame.rect.Rect(mermaid.rectangle[0] + mermaid.rectangle[1],mermaid.rectangle[1] + int(mermaid.rectangle[3]/2),int(mermaid.rectangle[2]/5),int(mermaid.rectangle[3]/5))
        self.image=pygame.transform.scale(pygame.image.load("images/hook4x"), (self.rectangle[2],self.rectangle[3]))
    def draw(self,screen):
        self.rectangle[0]=self.rectangle[0]+self.mx*3
        self.rectangle[1]=self.rectangle[1]+self.my*3
        screen.blit(self.image,self.rectangle)