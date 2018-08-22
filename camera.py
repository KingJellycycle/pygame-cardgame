import pygame
from random import randint

class Camera():
    # This also is a problem, When grouping items together, the camera only sends them has seperate items...
    # Can add a value to the second area the rect as 0/1 or something ot indicate that the send object are a group and render
    # then as so? need to figure this out
    BackgroundColour = [27,18,46]

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.surface = pygame.Surface((self.size))
        self.Scenes = []

    def scale(self, num):
        pass

    def newScene(self,name,objects,Zindex,render):        
        self.Scenes.append([name,objects,Zindex,render])

    def changeToScene(self,name):
        for Scenes in self.Scenes:
            Scenes[3] = False
            if Scenes[0] == name:
                Scenes[3] = True

    def addObject(self, target, object):
        for x in range(0,len(self.Scenes)):
            if self.Scenes[x][0] == target:
                self.Scenes[x][1].append(object)

    def shakeCamera(self,amount,zoom):
        global gameClock
        # Amount is Seconds
        currentTime = gameClock
        while (gameClock <= currentTime+amount):
            print("shake")            

    # Run draw methods of each elements
    def update(self,window):
        self.surface.fill(Camera.BackgroundColour, (self.pos[0],self.pos[1],self.size[0],self.size[1]))
        
        for Scenes in self.Scenes:
            if Scenes[3] == True:
                for objects in Scenes[1]:
                    if objects.type == "UI":
                        objects.update()
                        objects.draw(self.pos)
                    if objects.type == "game":
                        objects.update()
                        objects.draw()
        window.blit(self.surface,self.pos)