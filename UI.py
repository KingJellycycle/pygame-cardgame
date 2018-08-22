import pygame

class UI():
    pygame.font.init()
    camera = None
             #Text          Button BG     Button Hover Button click
    theme = [(255,255,255),(150,150,150),(100,100,100),(75,75,75)]
    elements = []
    
    def __init__(self,camera):
        UI.camera = camera

class Text(UI):
    
    def __init__(self,text,size,colour,target,pos):
        self.type = "UI"
        self.size = size
        self.pos = pos
        self.baseColour = colour
        self.hasBorder = False
        self.visable = True
        self.text = text
        self.target = target
        self.font = pygame.font.SysFont(None, self.size)
        self.textSurface = self.font.render(self.text, True, self.baseColour)
        self.textRect = self.textSurface.get_rect()
        UI.camera.addObject(self.target,self)
    
    def update(self):
        self.textSurface = self.font.render(self.text, True, self.baseColour)
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = self.pos

    def draw(self,pos):
        self.camera.surface.blit(self.textSurface,self.textRect)

class Button(UI):

    def __init__(self,text,size,target,pos,action,layer=0,parentPos=None):
        self.type = "UI"
        self.text = text
        self.textColour = UI.theme[0]
        self.size = size
        self.target = target
        self.pos = pos
        self.action = action
        self.colour = UI.theme[1]
        self.defaultColour = UI.theme[1]
        self.hoverColour = UI.theme[2] 
        self.clickColour = UI.theme[3]

        UI.camera.addObject(self.target,self)
        
        self.text = Text(text,self.size[2],self.textColour,self.target,self.pos)

        UI.elements.append(self)

    def update(self):
        if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[0]+self.size[0] and pygame.mouse.get_pos()[1] > self.pos[1] and pygame.mouse.get_pos()[1] < self.pos[1]+self.size[1]:
            if pygame.mouse.get_pressed()[0]:
                self.colour = self.clickColour
                eval(self.action)
            else:
                self.colour = self.hoverColour
        else:
            self.colour = self.defaultColour

        self.text.pos = [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]/2]

    def draw(self,pos):
        pygame.draw.rect(UI.camera.surface,self.colour,(pos[0]+self.pos[0],pos[1]+self.pos[1],self.size[0],self.size[1]))