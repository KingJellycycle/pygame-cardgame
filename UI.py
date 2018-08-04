import pygame
class UI():
    camera = None

    def __init__(self,camera):
        UI.camera = camera

    def createText(self,text,size,target,pos,layer):
        font = pygame.font.SysFont(None, size)
        self.render = font.render(text, True, (200, 200, 200))
        self.renderrect = self.render.get_rect()
        self.renderrect.centerx = pos[0]
        self.renderrect.centery = pos[1]

        UI.camera.addObject(target,[self.render,self.renderrect])
