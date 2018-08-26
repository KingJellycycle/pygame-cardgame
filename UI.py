import pygame

class UI():
    #pygame.font.init()
    camera = None
             #Text          Button BG     Button Hover Button click Panel BG
    theme = [
        # Text
        (255,255,255),
        # Button Background
        (150,150,150),
        # Button Hover
        (100,100,100),
        # Button Click
        (75,75,75),
        # Panel Background
        (20,20,20)
        ]
    elements = []
    layerRange = 0
    
    def __init__(self,camera):
        UI.camera = camera
        
    def wrapText(self, surface, size, text, pos, font=None, color=pygame.Color('black')):
        if not font:
            font = pygame.font.SysFont(None, self.size)
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = size[0],size[1]
        x, y = pos
        
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = size[0],size[1]
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

class Text(UI):
    
    def __init__(self,text,size,colour,target,pos,hasParent=False,layer=None,wrapping=None):
        self.type = "UI"
        self.size = size
        self.pos = pos
        self.baseColour = colour
        self.hasBorder = False
        self.text = text
        self.target = target
        self.textSurface = pygame.font.SysFont(None, self.size).render(self.text, True, self.baseColour)
        self.wrapping = wrapping
        
        self.visible = True
        self.textRect = self.textSurface.get_rect()

        if layer == None:
            self.layer = self.camera.layerRange
            self.camera.layerRange += 1
        #elif layer > self.camera.layerRange:

        if not hasParent:
            UI.camera.addObject(self.target,self)
        else:
            pass
    
    def update(self):
        self.textSurface = pygame.font.SysFont(None, self.size).render(self.text, True, self.baseColour)
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = self.pos

    def draw(self):
        if not self.wrapping:
            self.camera.surface.blit(self.textSurface,self.textRect)
        else:
            self.wrapText(self.camera.surface,[self.wrapping,5],self.text,self.pos,None,self.baseColour)

    def destory(self):
        del self

class Button(UI):

    def __init__(self,text,size,target,pos,action=None,layer=None):
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

        self.visible = True
        self.pressed = False

        if layer == None:
            self.layer = self.camera.layerRange
            self.camera.layerRange += 1

        self.text = Text(text,self.size[2],self.textColour,self.target,self.pos,True)

        UI.camera.addObject(self.target,self)

    def update(self):
        
        if pygame.mouse.get_pos()[0] > UI.camera.pos[0] + self.pos[0] and pygame.mouse.get_pos()[0] < UI.camera.pos[0] + self.pos[0]+self.size[0] and pygame.mouse.get_pos()[1] > UI.camera.pos[1] + self.pos[1] and pygame.mouse.get_pos()[1] < UI.camera.pos[1] + self.pos[1]+self.size[1]:
            if pygame.mouse.get_pressed()[0]:
                if self.pressed:
                    pass
                else:
                    self.colour = self.clickColour
                    if self.action == None:
                        pass
                    else:
                        for functionNum in range(0,int(len(self.action))):

                            if self.action[functionNum][1] == []:
                                self.action[functionNum][0]()
                            else: 
                                self.action[functionNum][0](*self.action[functionNum][1])
                self.pressed = True
            else:
                self.pressed = False
                self.colour = self.hoverColour
        else:
            self.colour = self.defaultColour
        
        self.text.pos = [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]/2]
        self.text.update()

    def draw(self):
        pygame.draw.rect(UI.camera.surface,self.colour,(self.pos[0],self.pos[1],self.size[0],self.size[1]))
        self.text.draw()
        pass

    def changeVisibility(self,state=None):
        if state == None:
            if self.visible:
                self.visible = False
                self.text.visible = False
            else:
                self.visible = True
                self.text.visible = True
        else:
            self.visible = state
        
        self.text.visible = self.visible

    def destory(self):
        self.text.destory()
        del self


class Panel(UI):
    def __init__(self,size,target,pos,layer=None):
        self.type = "UI"
        self.colour = UI.theme[4]
        self.size = size
        self.target = target
        self.pos = pos
        self.visible = True

        if layer == None:
            self.layer = self.camera.layerRange
            self.camera.layerRange += 1

        self.camera.addObject(self.target,self)

    def draw(self):
        pygame.draw.rect(UI.camera.surface,self.colour,(self.pos[0],self.pos[1],self.size[0],self.size[1]))

    def update(self):
        pass

    def destory(self):
        del self

"""
class Card(UI):
    def __init__(self,name,description,cost,size,target,pos,layer=0,parentPos=None):
        self.type = "UI"
        self.name = name
        self.description
        self.textColour = UI.theme[0]
        self.size = size
        self.target = target
        self.pos = pos
        self.action = action
        self.colour = UI.theme[1]

        UI.camera.addObject(self.target,self)
        
        self.text = Text(text,self.size[2],self.textColour,self.target,self.pos)

        UI.elements.append(self)

    def update(self):
        if UI.camera.pos[0] + pygame.mouse.get_pos()[0] > self.pos[0] and UI.camera.pos[0] + pygame.mouse.get_pos()[0] < self.pos[0]+self.size[0] and UI.camera.pos[1] + pygame.mouse.get_pos()[1] > self.pos[1] and UI.camera.pos[1] + pygame.mouse.get_pos()[1] < self.pos[1]+self.size[1]:
            if pygame.mouse.get_pressed()[0]:
                self.colour = self.clickColour
                for functionNum in range(0,len(self.action)/2):
                    print(functionNum)
            else:
                self.colour = self.hoverColour
        else:
            self.colour = self.defaultColour

        self.text.pos = [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]/2]

    def draw(self):
        pygame.draw.rect(UI.camera.surface,self.colour,(self.pos[0],self.pos[1],self.size[0],self.size[1]))
"""