import pygame

print("cards.py - Creating Cards!")

class Card:
    cardlist = []
    def __init__(self, name, image, title, description, cost):
        self.name = name
        self.image = image
        self.title = title
        self.description = description
        self.cost = cost

        Card.cardlist.append(self)

class Champion(Card):

    def __init__(self, name, image, title, description, attack, health, cost, onplay=None,passive=None):
        self.health = health
        self.attack = attack
        self.onplay = onplay
        self.passive = passive

        Card.__init__(self, name, image, title, description, cost)


class Unit(Champion):
    def __init__(self, name, image, title, description, attack, health, cost, onplay=None,passive=None):
        self.isUnit = True

        Champion.__init__(self, name, image, title, description, attack, health, cost, onplay=None,passive=None)

class Spell(Card):
    
    def __init__(self, name, image, title, description, cost, onplay=None, passive=None):
        self.onplay = onplay
        self.passive = passive

        Card.__init__(self, name, image, title, description, cost)

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
