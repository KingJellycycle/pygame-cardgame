import pygame
from textwrap import fill
from UI import *

class Cards:
    camera = None
    cardlist = []
    deco = [    
        #pygame.image.load("./assets/images/cards/deco/Overlay.png"),
        #pygame.image.load("./assets/images/cards/deco/Back.png"),
        #pygame.image.load("./assets/images/cards/deco/Border.png")
    ]
    target = "Game"
    size = [480,672]

    def __init__(self, name, image, title, description, cost, pos):
        self.name = name
        self.image = image
        self.title = title
        self.description = description
        self.cost = cost
        self.pos = pos
        self.visible = False

        self.scale = 1

        self.layer = self.camera.layerRange
        self.camera.layerRange += 1

        Cards.cardlist.append(self)

    def update(self):
        pass

    def event(self,event):
        pass

    def draw(self):
        pygame.draw.rect(self.camera.surface,[27,18,46],(self.pos[0],self.pos[1],self.size[0]*self.scale,self.size[1]*self.scale))

class Champion(Cards):

    def __init__(self, name, image, title, description, attack, health, cost, pos, onplay=None,passive=None):
        self.type = "UI"
        self.health = health
        self.attack = attack
        self.onplay = onplay
        self.passive = passive
        self.bgColourDefault = (150,50,50)
        self.bgColour = self.bgColourDefault
        self.bgSelected = (200,255,200)
        self.defaultColour = (200,200,200)
        self.colour = self.defaultColour
        self.clickColour = (255,255,255)
        self.hoverColour = (100,100,100)
        self.selected = False
        self.isSelected = False
        self.isPressed = False
        self.active = False
        self.click = False

        Cards.__init__(self, name, image, title, description, cost, pos)
        
        self.text = [
            Text(self.name,(0,0),80,(255,255,255),"Game",False,True,self.layer+1),
            Text(self.title,(0,0),50,(255,255,255),"Game",False,True,self.layer+1),
            Text(self.description,(0,0),50,(255,255,255),"Game",False,True,self.layer+1),
            Text(str(self.cost),(0,0),80,(255,255,255),"Game",False,True,self.layer+1),
            Text(str(self.health),(0,0),80,(255,100,100),"Game",False,True,self.layer+1),
            Text(str(self.attack),(0,0),80,(100,100,100),"Game",False,True,self.layer+1),
        ]

        for item in self.text:
            item.visible = False

    def update(self):
        if self.click:
            if self.active:
                self.selected = True
                self.isPressed = True
        else:
            self.isPressed = False
            self.selected = False
                
        if self.active:
            self.bgColour = (255,255,255)
        else:
            self.bgColour = self.bgColourDefault
            
        #self.text.pos = [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]/2]

    def draw(self):
        # Background
        if self.isSelected:
            pygame.draw.rect(self.camera.surface,(50,50,50),(self.pos[0],self.pos[1],self.size[0]*self.scale,self.size[1]*self.scale))
        else:
            pygame.draw.rect(self.camera.surface,self.bgColour,(self.pos[0],self.pos[1],self.size[0]*self.scale,self.size[1]*self.scale))
        # Name
        self.text[0].pos = [self.pos[0]+(25*self.scale),self.pos[1]+(315*self.scale)]
        pygame.draw.rect(self.camera.surface,self.colour,(self.pos[0]+(15*self.scale),self.pos[1]+(300*self.scale),max(200, self.text[0].textRect[2]+25)*self.scale,75*self.scale))
        
        # Title
        self.text[1].pos = [self.pos[0]+(25*self.scale),self.pos[1]+(400*self.scale)]
        #self.text[1].wrapping = (50*self.scale)
        pygame.draw.rect(self.camera.surface,self.colour,(self.pos[0]+(15*self.scale),self.pos[1]+(380*self.scale),max(200, self.text[1].textRect[2]+5)*self.scale,75*self.scale))
        
        # Description
        self.text[2].pos = [self.pos[0]+(20*self.scale),self.pos[1]+(470*self.scale)]
        #self.text[2].wrapping = (500*self.scale)
        pygame.draw.rect(self.camera.surface,self.colour,(self.pos[0]+(15*self.scale),self.pos[1]+(460*self.scale),450*self.scale,200*self.scale))
        
        # Cost
        self.text[3].pos = [self.pos[0]+(37*self.scale),self.pos[1]+(30*self.scale)]
        pygame.draw.circle(self.camera.surface,self.colour,[int(self.pos[0]+(55*self.scale)),int(self.pos[1]+(55*self.scale))],int(50*self.scale))

        # Health
        self.text[4].pos = [self.pos[0]+(300*self.scale),self.pos[1]+(30*self.scale)]
        self.text[4].Text (str(self.health))
        # Attack
        self.text[5].pos = [self.pos[0]+(300*self.scale),self.pos[1]+(100*self.scale)]
        self.text[5].Text (str(self.attack))
        #print(self.scale)
        for item in self.text:
            item.Scale(self.scale)
            item.update()
            item.draw()
        
        self.isSelected = False

    def event(self,event):
        if pygame.mouse.get_pos()[0] > UI.camera.pos[0] + self.pos[0] and pygame.mouse.get_pos()[0] < UI.camera.pos[0] + self.pos[0]+(self.size[0]*self.scale) and pygame.mouse.get_pos()[1] > UI.camera.pos[1] + self.pos[1] and pygame.mouse.get_pos()[1] < UI.camera.pos[1] + self.pos[1]+(self.size[1]*self.scale):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.click = False
            else:
                self.click = False

    def changeVisibility(self,state=None):
        if state == None:
            if self.visible:
                self.visible = False
            else:
                self.visible = True
        else:
            self.visible = state
        
        for item in self.text:
            item.visible = self.visible

class Unit(Champion):
    def __init__(self, name, image, title, description, attack, health, cost, pos, onplay=None,passive=None):
        self.isUnit = True

        Champion.__init__(self, name, image, title, description, attack, health, cost, pos, onplay=None,passive=None)
    
    def draw(self):
        pass

class Spell(Cards):
    
    def __init__(self, name, image, title, description, cost, pos, onplay=None, passive=None):
        self.onplay = onplay
        self.passive = passive

        Cards.__init__(self, name, image, title, description, cost, pos)
    
    def draw(self):
        pass

class Slot(Cards):

    def __init__(self):
        self.pos = [0,0]
        self.health = 1
        self.attack = 0
        self.scale = 1
        self.selected = False
        self.click = False
        self.active = False
        self.bgColour = (50,50,50)

    def draw(self):
        pygame.draw.rect(self.camera.surface,self.bgColour,(self.pos[0],self.pos[1],self.size[0]*self.scale,self.size[1]*self.scale))

    def update(self):
        if self.click:
            self.selected = True
        else:
            self.selected = False

        if self.active:
            self.bgColour = (100,100,100)
        else:
            self.bgColour = (50,50,50)
        pass
    
    def event(self,event):
        if pygame.mouse.get_pos()[0] > UI.camera.pos[0] + self.pos[0] and pygame.mouse.get_pos()[0] < UI.camera.pos[0] + self.pos[0]+(self.size[0]*self.scale) and pygame.mouse.get_pos()[1] > UI.camera.pos[1] + self.pos[1] and pygame.mouse.get_pos()[1] < UI.camera.pos[1] + self.pos[1]+(self.size[1]*self.scale):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True
            else:
                self.click = False

    def changeVisibility(self,value):
        pass

champions = [
    #name,image,title,description,attack,health,cost,onplay,passive
    ["Azir","Azir","The Emperor of the Sands","On-play: Summons 1 Sand Soldier Sand Soldiers - 3 Attack, 1 Health",2,2,3],
    ["Braum","Braum","The Heart of Freljord","On-play: Becomes a Taunt unit.",2,6,3],
    ["Kindred","Kindred","The Eternal Hunters","On-play: This unit can prevent the death of any unit selected Last for 1 turn. Passive: Wolf will mark a random enemy unit if the marked unit is killed Gain 3 Attack.",1,3,4],
    ["MinionC","Minion","Caster","Caster minion!",3,1,2],
    ["MinionM","Minion1","Melee","Melee minion!",1,2,1],
    ["MinionS","Minion2","Seige","Seige minion!",3,3,3]
]

spells = [
    ["Heal", None, None, "Heals a unit for 1 Health",3]
]

units = [
    ["Sand Soldier","Azir","The Emperor's Follower","Summoned By Azir Himself",3,1,0],
]

#Creates one of each card for deck building purposes
def cardInit(camera):
    
    print("cards.py - Creating Cards!")
    Cards.camera = camera
    
    for cards in champions:
        Champion(*cards,[0,0])


    #for cards in spells:
    #    Spell(*cards,[0,0])

#These cards can be created by the summoner of these unit
#for cards in units:
    #Unit(*cards)