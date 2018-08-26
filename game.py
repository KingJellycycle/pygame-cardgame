import pygame
from UI import *
from camera import *
from player import *
from cards import *
import copy

class Game():
    
    def __init__(self,window,camera):
        print("game.py - Initialising game.py and various other setup things!")
        self.camera = camera
        self.type = "game"
        self.target = "Game"
        self.window = window
        self.phase = "Summon"
        self.selectedCard = None
        self.targetCard = None
        self.colours = [
            # Health
            (255,20,20),
            # Armor 
            (110,100,110),
            # Mana
            (20,20,255)
        ]
        self.turn = [0,0]
        self.board = pygame.image.load('./assets/images/Board.png')
        self.layer = -1
        self.players = [
            Player("one",self.getStandardDeck(),30,0,0,1,10),
            Player("two",self.getStandardDeck(),30,0,0,1,10)
        ]
        self.UI = {
            "TurnCounter": Text("Turn: "+str(self.turn[0]),24,UI.theme[0],self.target,[window.get_size()[0]-80,window.get_size()[1]/2-35]),
            "EndTurnButton": Button("End Turn!",[150,50,24],self.target,[window.get_size()[0]-150-5,window.get_size()[1]/2-25],[[self.changeTurn,[]]]),
            "CurrentPlayer": Text("Playing: ",24,UI.theme[0],self.target,[window.get_size()[0]-80,window.get_size()[1]/2-55]),
            
            # Player top text
            "TOPpanel": Panel([450,150],self.target,[50,0]),
            "TOPplayer": Button("Player Top",[300,100,24],self.target,[window.get_size()[0]-350,0],[[self.attack,[self.players[1],5]]]),
            "TOPhealth": Text("HealthT",48,self.colours[0],self.target,[window.get_size()[0]-330,115]),
            "TOParmor": Text("ArmorT",48,self.colours[1],self.target,[window.get_size()[0]-65,115]),
            "TOPmana": Text("ManaT",48,self.colours[2],self.target,[window.get_size()[0]-550,130]),
            
            # Player bottom text
            "BOTTOMpanel": Panel([450,150],self.target,[window.get_size()[0]-500,window.get_size()[1]-150]),
            "BOTTOMplayer": Button("Player Bottom",[300,100,24],self.target,[65,window.get_size()[1]-100],[[self.attack,[self.players[0],5]]]),
            "BOTTOMhealth": Text("HealthB",48,self.colours[0],self.target,[90,window.get_size()[1]-115]),
            "BOTTOMarmor": Text("ArmorB",48,self.colours[1],self.target,[350,window.get_size()[1]-115]),
            "BOTTOMmana": Text("ManaB",48,self.colours[2],self.target,[window.get_size()[0]-75,window.get_size()[0]-380]),

            "BACK": Button("Back",[50,50,24],self.target,[100,100],[[self.camera.changeToScene,["Main Menu"]]]),
            "Winner": Text("Match",50,(255,255,255),self.target,(self.camera.surface.get_size()[0]/2,self.camera.surface.get_size()[1]/2)),

            #Card("YEDUASDSDAHJSDAhujS","TADS","ASD",3,2,2,[133,200,24],self.target,[200,200],None)'''
        }
        self.table = [
            #Player 1
            [self.getCard(0),None,None,None],
            #Player 2
            [None,None,None,None]
        ]
        self.UI["Winner"].visible = False

        print("game.py - Player 1: ",self.players[0])
        print("")
        print("game.py - Player 2: ",self.players[1])
        print("=========================================")
        print("game.py - Player 1 Hand: ",self.players[0].deck)
        print("")
        print("game.py - Player 2 Hand: ",self.players[1].deck)
        print("=========================================")
        print("")

        self.changeTurn()
        self.camera.addObject(self.target,self)
        
    def destory(self):
        for item in self.UI:
            self.UI[item].destory()
        
        Cards.cardlist = []
        self.camera.cleanScene("Game")
        self.camera.destoryScene("Game")
        del self
        

    def drawHand(self):
        # for each card in the card list call its draw function
        #for cards in Card.cardlist:
        #    cards.draw()
        pass

    def updateUI(self):
        self.UI["TurnCounter"].text = "Turn: "+str(self.turn[0])
        self.UI["CurrentPlayer"].text = "Playing: " + str(self.players[self.turn[1]].name)

        self.UI["TOPhealth"].text = str(self.players[1].health)
        self.UI["TOParmor"].text = str(self.players[1].armor)
        self.UI["TOPmana"].text = str(self.players[1].mana) + "/" + str(self.players[1].currentMaxMana)

        self.UI["BOTTOMhealth"].text = str(self.players[0].health)
        self.UI["BOTTOMarmor"].text = str(self.players[0].armor)
        self.UI["BOTTOMmana"].text = str(self.players[0].mana) + "/" + str(self.players[0].currentMaxMana)

    def update(self):
        self.drawHand()
        self.updateUI()
        self.camera.surface.blit(self.board,(0,0))
        for card in self.table[0]:
            len(self.table)
            if card == None:
                pass
            else:
                card.pos = [187,189]
                card.scale = 0.25
                card.changeVisibility(True)
                card.draw()
                card.update(self.selectedCard)

        self.endgame(self.players)
    
    def draw(self):
        pass

    def endgame(self,player):
        end = False
        if player[0].health <= 0 and player[1].health <= 0:
            end = True
            self.UI["Winner"].text = "Match - Draw"
            for item in self.UI:
                self.UI[item].visible = False
            for card in self.table[0]:
                if card == None:
                    pass
                else:
                    card.changeVisibility(False)
            for card in self.table[1]:
                if card == None:
                    pass
                else:
                    card.changeVisibility(False)
            
            self.UI["Winner"].visible = True

        elif player[0].health <= 0:
            end = True
            self.UI["Winner"].text = "Match - Winner: " + player[1].name
            for item in self.UI:
                self.UI[item].visible = False
            for card in self.table[0]:
                if card == None:
                    pass
                else:
                    card.changeVisibility(False)
            for card in self.table[1]:
                if card == None:
                    pass
                else:
                    card.changeVisibility(False)
        
        elif player[1].health <= 0:
            end = True
            self.UI["Winner"].text = "Match - Winner: " + player[0].name
            for item in self.UI:
                self.UI[item].visible = False
            for card in self.table[0]:
                if card == None:
                    pass
                else:
                    card.changeVisibility(False)
            for card in self.table[1]:
                if card == None:
                    pass
                else:
                    card.changeVisibility(False)

        if end:
            self.UI["Winner"].visible = True

            self.UI["BACK"].visible = True
            self.UI["BACK"].size = (200,75,24)
            self.UI["BACK"].pos = (self.camera.surface.get_size()[0]/2-(self.UI["BACK"].size[0]/2),self.camera.surface.get_size()[1]/2+100)

    def attack(self,unit,card):
        unit.health -= card
        
    def changeTurn(self):
        if self.turn[1] == 1:
            self.turn[1] = 0
        else:
            self.turn[1] = 1
            
        self.turn[0] += 1

    def getCard(self,position):
        card = copy.copy(Cards.cardlist[position])
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
		
    def destoryCard(self,card):
        del card

    def getStandardDeck(self):
        return [
            # Units
                #[self.getCard(0),5],
                #[self.getCard(1),5],
                #[self.getCard(2),5],
                #[self.getCard(3),5],
                #[self.getCard(4),5],
                #[self.getCard(5),5]       
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