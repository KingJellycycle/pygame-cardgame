import pygame
from random import randint

class Camera():

    Scenes = []
    BackgroundColour = [27,18,46]

    def __init__(self, surface, pos, size):
        self.surface = surface
        self.pos = pos
        self.size = size

    def scale(self, num):
        pass

    def newScene(self,name,objects,Zindex,render):        
        Camera.Scenes.append([name,objects,Zindex,render])

    def addObject(self, target, object):
        for x in range(0,len(Camera.Scenes)):
            if Camera.Scenes[x][0] == target:
                Camera.Scenes[x][1].append(object)

    def shakeCamera(self,amount,zoom):
        global gameClock
        # Amount is Seconds
        currentTime = gameClock
        while (gameClock <= currentTime+amount):
            print("shake")            
        pass

    def draw(self):
        for Scenes in Camera.Scenes:
            if Scenes[3] == True:
                self.surface.fill(Camera.BackgroundColour, (self.pos[0],self.pos[1],self.size[0],self.size[1]))
                for objects in Scenes[1]:
                    self.surface.blit(objects[0],(self.pos[0]+objects[1][0],self.pos[1]+objects[1][1]))