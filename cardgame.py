from random import randint
from cards import *
from player import *

class cardgame:

    def __init__(self):
        print("cardgame.py - Initialising Cardgame.py and various other setup things!")
        
        self.cardlist = []
        self.turn = [0,0]

        self.table = [
            #Player 1
            [],
            #Player 2
            []
        ]
        
        self.spells = [                
                ["Heal", "Heals selected Unit",3],
                ["Cleanse", "Removes Status Effects",1],
                ["Snowball", "1 dmg to selected unit",1]
        ]

        self.debuffs = [
            ["Burn"],
            ["Stun"]
        ]

        self.players = [
            [Player("one",self.getStandardDeck(),30,0,0)],
            [Player("two",self.getStandardDeck(),30,0,0)]
        ]
        
        print("cardgame.py - Player 1: ",self.players[0])
        print("")
        print("cardgame.py - Player 2: ",self.players[1])
        print("=========================================")
        print("cardgame.py - Player 1 Hand: ",self.players[0][0].deck)
        print("")
        print("cardgame.py - Player 2 Hand: ",self.players[1][0].deck)
        print("=========================================")
        print("")

    def draw(self,surface):
        pass

    def update(self):
        pass

	#
    def getCard(self,position):
        return Card.cardlist[position]

    def drawCard(self,target,amount=1,type=-1):
        for x in range(0,amount):
            if (len(target.hand) <= 6):
                y = randint(0,len(target.deck)-1)
                target.deck[y][1] -= 1
                target.hand.append(target.deck[y][0])
            else:
                y = randint(0,len(target.deck)-1)
                target.deck[y][1] -= 1
        
        if (target.deck[y][1] <= 0):
            del target.deck[y]
            

    def summonCard(self,entity,amount=1,location=-1):
        # Summons a card
        for x in range(0,amount):
            print("Summoned - ",entity.name)
            self.table[self.turn[1]].append(entity)

    def playCard(self,card,location):
        self.table[self.turn[1]].append(card)
        del card
		
    def destoryCard(self,entity):
        pass

    def getStandardDeck(self):
        return [
            # Units
                [self.getCard(0),5],
                [self.getCard(1),5],
                [self.getCard(2),5],
                [self.getCard(3),5],
                [self.getCard(4),5],
                [self.getCard(5),5]       
        ]