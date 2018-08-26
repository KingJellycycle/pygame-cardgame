import pygame
from textwrap import fill
from UI import *

class Cards:
    cardlist = []
    deco = [    
        pygame.image.load("./assets/images/cards/deco/Overlay.png"),
        pygame.image.load("./assets/images/cards/deco/Back.png"),
        pygame.image.load("./assets/images/cards/deco/Border.png")
    ]
    target = "Game"
    overlaySurface = pygame.Surface([1024,768], pygame.SRCALPHA, 32)
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

        Cards.cardlist.append(self)

    def draw(self):
        UI.camera.surface.blit(self.overlaySurface,[0,0])

    def cleanup(self):
        self.cardlist = []

class Champion(Cards):

    def __init__(self, name, image, title, description, attack, health, cost, pos, onplay=None,passive=None):
        self.health = health
        self.attack = attack
        self.onplay = onplay
        self.passive = passive
        self.bgColourDefault = (100,255,100)
        self.bgColour = self.bgColourDefault
        self.bgSelected = (200,255,200)
        self.defaultColour = (200,200,200)
        self.colour = self.defaultColour
        self.clickColour = (255,255,255)
        self.hoverColour = (100,100,100)

        Cards.__init__(self, name, image, title, description, cost, pos)

        self.text = [
            Text(self.name,24,(255,255,255),"Game",(0,0)),
            Text(self.title,10,(255,255,255),"Game",(0,0)),
            Text(self.description,24,(255,255,255),"Game",(0,0)),
            Text(str(self.cost),24,(255,255,255),"Game",(0,0)),
        ]
        for item in self.text:
            item.visible = False


    def update(self,select):
        if pygame.mouse.get_pos()[0] > UI.camera.pos[0] + self.pos[0] and pygame.mouse.get_pos()[0] < UI.camera.pos[0] + self.pos[0]+(self.size[0]*self.scale) and pygame.mouse.get_pos()[1] > UI.camera.pos[1] + self.pos[1] and pygame.mouse.get_pos()[1] < UI.camera.pos[1] + self.pos[1]+(self.size[1]*self.scale):
            if pygame.mouse.get_pressed()[0]:
                select = self
                self.bgColour = self.bgSelected
            else:
                self.bgColour = self.bgColourDefault


        #self.text.pos = [self.pos[0]+self.size[0]/2,self.pos[1]+self.size[1]/2]

    def draw(self):
        # Background UI.camera.surface
        pygame.draw.rect(self.overlaySurface,self.bgColour,(self.pos[0],self.pos[1],self.size[0]*self.scale,self.size[1]*self.scale))
        # Name
        self.text[0].pos = [self.pos[0]+(110*self.scale),self.pos[1]+(340*self.scale)]
        self.text[0].size = int(80*self.scale)
        pygame.draw.rect(self.overlaySurface,self.colour,(self.pos[0]+(15*self.scale),self.pos[1]+(300*self.scale),200*self.scale,75*self.scale))
        # Title
        self.text[1].pos = [self.pos[0]+(115*self.scale),self.pos[1]+(420*self.scale)]
        self.text[1].size = int(24*self.scale)
        pygame.draw.rect(self.overlaySurface,self.colour,(self.pos[0]+(15*self.scale),self.pos[1]+(380*self.scale),200*self.scale,75*self.scale))
        # Description
        self.text[2].pos = [self.pos[0]+(25*self.scale),self.pos[1]+(460*self.scale)]
        self.text[2].size = int(60*self.scale)
        self.text[2].wrapping = (2000*self.scale)
        pygame.draw.rect(self.overlaySurface,self.colour,(self.pos[0]+(15*self.scale),self.pos[1]+(460*self.scale),450*self.scale,200*self.scale))
        # Cost
        self.text[3].pos = [self.pos[0]+(50*self.scale),self.pos[1]+(50*self.scale)]
        self.text[3].size = int(80*self.scale)
        pygame.draw.circle(self.overlaySurface,self.colour,[int(self.pos[0]+(55*self.scale)),int(self.pos[1]+(55*self.scale))],int(50*self.scale))
        
        Cards.draw(self) 
        
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

champions = [
    #name,image,title,description,attack,health,cost,onplay,passive
    ["Azir","Azir","The Emperor of the Sands","On-play: Summons 1 Sand Soldier \nSand Soldiers - 3 Attack, 1 Health",2,2,3],
    ["Braum","Braum","The Heart of Freljord","On-play: Becomes a Taunt unit.",2,6,3],
    ["Kindred","Kindred","The Eternal Hunters","On-play: This unit can prevent the death of any unit selected (Last for 1 turn). :: Passive: Wolf will mark a random enemy unit if the marked unit is killed Gain 3 Attack.",1,3,4],
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
def cardInit():
    
    print("cards.py - Creating Cards!")
    for cards in champions:
        Champion(*cards,[0,0])

    #for cards in spells:
    #    Spell(*cards,[0,0])

#These cards can be created by the summoner of these unit
#for cards in units:
    #Unit(*cards)