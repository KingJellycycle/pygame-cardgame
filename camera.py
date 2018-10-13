import pygame

from random import randint

class Camera():

    layerRange = 0
    BackgroundColour = [27,18,46]

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.surface = pygame.Surface((self.size))
        self.Scenes = []

    def destory(self,window):
        for scenes in self.Scenes:
            self.destoryScene(scenes[0])
        window.fill([0,0,0])
        del self

    def cleanScene(self,name):
        for scene in self.Scenes:
            if scene[0] == name:
                scene[1] = []
        print("camera.py - Cleaned objects from Scene: ",name)
    
    def destoryScene(self,name):
        for scene in self.Scenes:
            if scene[0] == name:
                del scene
        print("camera.py - Destoryed Scene: ",name)

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
        self.surface.fill(Camera.BackgroundColour, (0,0,self.size[0],self.size[1]))
        for layer in range(-1,self.layerRange):
            for Scenes in self.Scenes:
                if Scenes[3] == True:
                    for objects in Scenes[1]:
                        if objects.layer == layer:
                            objects.update()
                            objects.draw()

        window.blit(self.surface,self.pos)

    # Runs event methods if available
    def event(self,event):
        for Scenes in self.Scenes:
            if Scenes[3] == True:
                for objects in Scenes[1]:
                    objects.event(event)