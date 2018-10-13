import pygame
pygame.font.init()
class UI():
    camera = None

    theme = [
        # Text
        (255,255,255),
        # Button Default
        (150,150,150),
        # Button Hover
        (100,100,100),
        # Button Click
        (75,75,75),
        # Panel Background
        (20,20,20)
        ]
    
    def __init__(self, pos, target, layer=None):
        self.pos = pos
        self.target = target

        if layer == None:
            self.layer = self.camera.layerRange
            self.camera.layerRange += 1

        # Auto Defined variables
        self.updated = True
        self.visible = True
        self.scale = 1

    def event(self,event):
        pass

    def destory(self):
        del self

    def hasParentCheck(self,hasParent):
        # Checks if it is required for the camera to render this object!
        if hasParent == False:
            self.camera.addObject(self.target,self)
        
    def wrapText(self, surface, size, text, pos, scale, font=None, color=pygame.Color('black')):
        #if not font:
        #    font = pygame.font.SysFont(None, int(self.size*scale))
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = size
        x, y = pos
        
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = font.size(word)[0],font.size(word)[1]
                if word_width >= max_width * self.scale:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

class Text(UI):
    
    def __init__(self,text,pos,size,colour,target,isCenter=True,hasParent=False,wrapLength=None,layer=None):
        self.size = size
        self.oldSize = size
        self.Textcolour = colour
        self.isCenter = isCenter
        self.text = text
        self.newText = text

        # Calls the very top most parent __init__() - UI
        super().__init__(pos,target,layer)

        self.textFont = pygame.font.Font("./assets/font/font.ttf",int(self.size*self.scale))
        self.textSurface = self.textFont.render(self.text, True, self.Textcolour)
        self.wrapLength = wrapLength

        self.textRect = self.textSurface.get_rect()

        # At the end of all child objects to check if the object is required to be rendered by the camera's method
        self.hasParentCheck(hasParent)

    def update(self):
        if self.visible:
            if self.isCenter:
                self.textRect.center = self.pos
            else:
                self.textRect.left = self.pos[0]
                self.textRect.top = self.pos[1]
            # Font problem occurs when closing the game, probably because it wants to update one last time
            # even though pygame.font has been destoryed
            #self.updateFont()

            #if not (self.newText == self.text):
            #    self.newText = self.text
            #    self.newScale = self.scale
            #    self.textSurface = pygame.font.SysFont(None, int(self.size*self.scale)).render(self.text, True, self.baseColour)
            #    self.textRect = self.textSurface.get_rect()
            #
            #if not (self.newScale == self.scale):
            #    self.newText = self.text
            #    self.newScale = self.scale
            #    self.textSurface = pygame.font.SysFont(None, int(self.size*self.scale)).render(self.text, True, self.baseColour)
            #    self.textRect = self.textSurface.get_rect()

    def draw(self):
        if self.visible:
        #if not self.wrapping:
            
            if self.updated:
                self.textFont = pygame.font.Font("./assets/font/font.ttf",int(round(self.size*self.scale,0)))
                self.textSurface = self.textFont.render(self.text, True, self.Textcolour)
            self.updated = False
            self.camera.surface.blit(self.textSurface,self.textRect)

        #else:
        #    self.wrapText(self.camera.surface,[self.wrapping,6],self.text,self.pos,self.scale,None,self.baseColour)

    # Ew! code
    def Scale(self,scale):
        self.updateUI(self.scale,scale)
        self.scale = scale

    def Text(self,text):
        self.updateUI(self.text,text)
        self.text = text

    def Size(self,size):
        self.updateUI(self.size,size)
        self.size = size

    def updateUI(self,original,new):
        if new == original:
            pass
        else:
            self.updated = True

class Button(Text):

    def __init__(self,text,pos,width,height,size,target,hasParent=False,action=None,colour=[UI.theme[1],UI.theme[2],UI.theme[3]],layer=None):
        
        self.colours = colour
        self.colour = self.colours[0]
        self.action = action
        self.pressed = False
        self.target = target

        self.rect = pygame.Rect(pos[0],pos[1],width,height)

        Text.__init__(self,text,[self.rect[0]+self.rect[2]/2,self.rect[1]+self.rect[3]/2],size,(255,255,255),target,True,True)
        
        self.hasParentCheck(hasParent)

    def update(self):
        if self.visible:
            if pygame.mouse.get_pos()[0] > UI.camera.pos[0] + self.rect[0] and pygame.mouse.get_pos()[0] < UI.camera.pos[0] + self.rect[0]+self.rect[2] and pygame.mouse.get_pos()[1] > UI.camera.pos[1] + self.rect[1] and pygame.mouse.get_pos()[1] < UI.camera.pos[1] + self.rect[1]+self.rect[3]:
                if pygame.mouse.get_pressed()[0]:
                    if self.pressed:
                        pass
                    else:
                        self.colour = self.colours[2]
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
                    self.colour = self.colours[1]
            else:
                self.colour = self.colours[0]

            Text.update(self)
            # Update Text Position
            self.pos = [self.rect[0]+self.rect[2]/2,self.rect[1]+self.rect[3]/2]
        pass

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.camera.surface,self.colour,self.rect)
            Text.draw(self)
        #self.text.draw()
        
        pass

    def changeVisibility(self,state=None):
        if state == None:
            if self.visible:
                self.visible = False
            else:
                self.visible = True
        else:
            self.visible = state

    def destory(self):
        Text.destory(self)
        super().destory()

class Input(UI):
    def __init__(self,pos,size,target,defaultText="",colour=UI.theme[0],layer=None):
        self.colour = colour
        self.text = defaultText
        self.txt_surface = pygame.font.Font("./assets/font/font.ttf", int(23)).render(self.text, True, self.colour)
        self.active = False

        super().__init__(pos,target,layer)

        self.rect = pygame.Rect(self.pos[0], self.pos[1], size[0], size[1])

        if layer == None:
            self.layer = self.camera.layerRange
            self.camera.layerRange += 1

        self.camera.addObject(self.target,self)
            
    def draw(self):
        if self.visible:
        # Blit the text & rect.
            self.camera.surface.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
            pygame.draw.rect(self.camera.surface, self.colour, self.rect, 2)

    def update(self):
        if self.visible:
            # Resize the box if the text is too long.
            width = max(200, self.txt_surface.get_width()+10)
            self.rect.w = width

    def event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.colour = UI.theme[1] if self.active else UI.theme[0]
        if event.type == pygame.KEYDOWN:
            if self.active:
                text = None
                if event.key == pygame.K_RETURN:
                    #print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    text = event.unicode
                if not text == None:
                    self.text += text
                text = None 
                # Re-render the text.
                self.txt_surface = pygame.font.Font("./assets/font/font.ttf", int(23)).render(self.text, True, self.colour)

class Panel(UI):
    def __init__(self,pos,width,height,target,hasParent=False,colour=UI.theme[4],layer=None):

        self.colour = colour
        self.rect = pygame.Rect(pos[0], pos[1], width, height)

        super().__init__(pos,target,layer)

        self.hasParentCheck(hasParent)

    def draw(self):
        pygame.draw.rect(self.camera.surface,self.colour,self.rect)

    def update(self):
        pass

'''
class ToolTip(Text):
    
    def __init__(self,text,pos,width,height,size,target,hasParent=False,colour=[UI.theme[1],UI.theme[2]],layer=None):
        self.colours = colour
        self.colour = self.colours[0]
        self.target = target

        self.rect = pygame.Rect(pos[0],pos[1],width,height)

        Text.__init__(self,text,[self.rect[0]+self.rect[2]/2,self.rect[1]+self.rect[3]/2],size,(255,255,255),target,True,True)
        
        self.hasParentCheck(hasParent)


    def update(self):
        if self.visible:
            if pygame.mouse.get_pos()[0] > UI.camera.pos[0] + self.rect[0] and pygame.mouse.get_pos()[0] < UI.camera.pos[0] + self.rect[0]+self.rect[2] and pygame.mouse.get_pos()[1] > UI.camera.pos[1] + self.rect[1] and pygame.mouse.get_pos()[1] < UI.camera.pos[1] + self.rect[1]+self.rect[3]:
                if pygame.mouse.get_pressed()[0]:
                    if self.pressed:
                        pass
                    else:
                        self.colour = self.colours[2]
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
                    self.colour = self.colours[1]
            else:
                self.colour = self.colours[0]

            Text.update(self)
            # Update Text Position
            self.pos = [self.rect[0]+self.rect[2]/2,self.rect[1]+self.rect[3]/2]
        pass

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.camera.surface,self.colour,self.rect)
            Text.draw(self)
        #self.text.draw()
        pass

    def changeVisibility(self,state=None):
        if state == None:
            if self.visible:
                self.visible = False
            else:
                self.visible = True
        else:
            self.visible = state

    def destory(self):
        Text.destory(self)
        super().destory()

'''