import pygame
from UI import *

print("cards.py - Creating Cards!")

class Cards:
    cardlist = []
    deco = [    
        pygame.image.load("./assets/images/cards/deco/Overlay.png"),
        pygame.image.load("./assets/images/cards/deco/Back.png"),
        pygame.image.load("./assets/images/cards/deco/Border.png")
    ]

    def __init__(self, name, image, title, description, cost, pos=[0,0]):
        self.name = name
        self.image = image
        self.title = title
        self.description = description
        self.cost = cost
        self.scale = 1
        self.pos = pos
        self.elements = [
            #Text(self.name,24,(225,255,255),"Game",self.pos)
        ]

        Cards.cardlist.append(self)

    def update(self):
        for element in self.elements:
            element.update()
            element.draw()

class Champion(Cards):

    def __init__(self, name, image, title, description, attack, health, cost, pos=[0,0], onplay=None,passive=None):
        self.health = health
        self.attack = attack
        self.onplay = onplay
        self.passive = passive

        Cards.__init__(self, name, image, title, description, cost, pos)

class Unit(Champion):
    def __init__(self, name, image, title, description, attack, health, cost, pos=[0,0], onplay=None,passive=None):
        self.isUnit = True

        Champion.__init__(self, name, image, title, description, attack, health, cost, pos, onplay=None,passive=None)
    
    def draw(self):
        pass

class Spell(Cards):
    
    def __init__(self, name, image, title, description, cost, pos=[0,0], onplay=None, passive=None):
        self.onplay = onplay
        self.passive = passive

        Cards.__init__(self, name, image, title, description, cost, pos)
    
    def draw(self):
        pass

champions = [
    #name,image,title,description,attack,health,cost,onplay,passive
    ["Azir","Azir","The Emperor of the Sands","On-play: Summons 1 Sand Soldier\n\nSand Soldiers - 3 Attack, 1 Health",2,2,3],
    ["Braum","Braum","The Heart of Freljord","On-play: Becomes a Taunt unit.",2,6,3],
    ["Kindred","Kindred","The Eternal Hunters","On-play: This unit can prevent the death of any unit selected (Last for 1 turn).\n\nPassive: Wolf will mark a random enemy unit if the marked unit is killed Gain 3 Attack.",1,3,4],
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
for cards in champions:
    Champion(*cards)

for cards in spells:
    Spell(*cards)

#These cards can be created by the summoner of these unit
#for cards in units:
    #Unit(*cards)


class CardElement():
    def __init__(self,name,description,cost,size,target,pos,layer=0,parentPos=None):
        self.type = "UI"
        self.size = size
        self.scale = 1
        self.nameText = name
        self.titleText = title
        self.descriptionText = description
        self.attackText = attack
        self.healthText = health
        self.costText = cost
        self.target = target
        self.colour = UI.theme[1]
        self.pos = pos
        self.layer = layer
        self.action = action
        self.parentPos = parentPos
        if self.parentPos == None:
            self.parentPos = [0,0]
    
        self.name = Text(self.nameText,self.size[2],self.colour,self.target,(self.pos[0]+(self.size[0]/2),20+self.pos[1]))
        self.title = Text(self.titleText,self.size[2],self.colour,self.target,(self.pos[0]+(self.size[0]/2),35+self.pos[1]))
        self.description = Text(self.descriptionText,self.size[2],self.colour,self.target,(self.pos[0]+(self.size[0]/2),50+self.pos[1]))
        self.attack = Text(str(self.attackText),self.size[2],self.colour,self.target,(self.pos[0]+(self.size[0]/2),65+self.pos[1]))
        self.health = Text(str(self.healthText),self.size[2],self.colour,self.target,(self.pos[0]+(self.size[0]/2),228800+self.pos[1]))
        self.cost = Text(str(self.costText),self.size[2],self.colour,self.target,(self.pos[0],200+self.pos[1]))
        
        UI.elements.append(self)
        #UI.camera.addObject(target,self)

    def draw(self,pos):
        pygame.draw.rect(UI.camera.surface,(0,0,0),(pos[0]+self.pos[0],pos[1]+self.pos[1],self.size[0],self.size[1]))
        self.name.draw(pos)
        self.title.draw(pos)
        self.description.draw(pos)
        self.attack.draw(pos)
        self.health.draw(pos)
        self.cost.draw(pos)
        
    def update(self):
        if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[0]+self.size[0] and pygame.mouse.get_pos()[1] > self.pos[1] and pygame.mouse.get_pos()[1] < self.pos[1]+self.size[1]:
            if pygame.mouse.get_pressed()[0]:
                self.colour = UI.theme[3]
                self.action()
            else:
                self.colour = UI.theme[2]
        else:
            self.colour = UI.theme[1]