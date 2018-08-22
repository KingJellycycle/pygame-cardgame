import pygame
from UI import *
from camera import *
from player import *
from cards import *

class Game():
    
    def __init__(self,window):
        print("game.py - Initialising game.py and various other setup things!")
        self.type = "game"
        self.target = "Game"
        self.window = window
        self.phase = "Summon"
        # have to move trhis below turn
        self.turn = [0,0]
        self.UI = [
            Text("Turn: "+str(self.turn[0]),24,UI.theme[1],self.target,[30,10]),
            #Card("YEDUASDSDAHJSDAhujS","TADS","ASD",3,2,2,[133,200,24],self.target,[200,200],None)
        ]
        #Copy the cards required for this game.
        self.cardlist = []

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
        
        print("game.py - Player 1: ",self.players[0])
        print("")
        print("game.py - Player 2: ",self.players[1])
        print("=========================================")
        print("game.py - Player 1 Hand: ",self.players[0][0].deck)
        print("")
        print("game.py - Player 2 Hand: ",self.players[1][0].deck)
        print("=========================================")
        print("")
        

    def draw(self):
        # for each card in the card list call its draw function
        #for cards in Card.cardlist:
        #    cards.draw()

        pass

    def update(self):
        self.UI[0].text = "Turn: "+str(self.turn[0])
        

	#
    def getCard(self,position):
        card = Cards.cardlist[position]
        return card

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

'''
#from player import *

cardgame = cardgame()

GS = 0
Phase = "Summon"

bg = pygame.image.load("./assets/images/board.png")
bgrect = bg.get_rect()

def draw():

    if (Phase == "Summon"):
        # Draw Cards
        #cardgame.draw(surface)

        pass
    
    if (Phase == "Attack"):
        pass
    
    if (Phase == "Swap"):
        turn[0] += 1
        if turn[1] == 1:
            turn[1] = 0
        else:
            turn[1] = 1

    pygame.display.flip()

def update():

    pass
'''