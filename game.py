import pygame
from UI import *
from camera import *
from player import *
from cards import *
import copy

class Game():
    
    def __init__(self,window,camera,player1,player2,HS):
        print("game.py - Initialising game.py and various other setup things!")
        self.gameloop = True
        self.camera = camera
        self.HS = HS
        self.target = "Game"
        self.window = window
        self.phase = "Summon"
        self.selectedUnit = None
        self.selectedCard = False
        self.targetUnit = None
        self.colours = [
            # Health
            (255,20,20),
            # Armor 
            (110,100,110),
            # Mana
            (20,20,255)
        ]
        self.turn = [0,0]
        self.board = pygame.Rect(0,0,1024,900) #pygame.image.load('')
        self.layer = -1
        self.players = [
            Player(player1[0],self.getStandardDeck(),30,0,0,1,10),
            Player(player2[0],self.getStandardDeck(),30,0,0,1,10)
        ]
        self.winner = None
        self.UI = {
            "TurnCounter": Text("Turn: "+str(self.turn[0]),[window.get_size()[0]-80,window.get_size()[1]/2-35],24,UI.theme[0],self.target),
            "EndTurnButton": Button("End Turn!",[window.get_size()[0]-150-5,window.get_size()[1]/2-25],150,50,24,self.target,False,[[self.changeTurn,[]]]),
            "CurrentPlayer": Text("Playing: ",[window.get_size()[0]-80,window.get_size()[1]/2-55],24,UI.theme[0],self.target),
            
            # Player top text
            #"TOPpanel": Panel([50,0],450,150,self.target),
            "TOPplayer": Button(self.players[0].name,[window.get_size()[0]-350,0],300,100,24,self.target,False),
            "TOPhealth": Text("HealthT",[window.get_size()[0]-330,115],48,self.colours[0],self.target),
            "TOParmor": Text("ArmorT",[window.get_size()[0]-65,115],48,self.colours[1],self.target),
            "TOPmana": Text("ManaT",[window.get_size()[0]-550,130],48,self.colours[2],self.target),
            
            # Player bottom text
            #"BOTTOMpanel": Panel([window.get_size()[0]-500,window.get_size()[1]-150],450,150,self.target),
            "BOTTOMplayer": Button(self.players[1].name,[65,window.get_size()[1]-100],300,100,24,self.target,False),
            "BOTTOMhealth": Text("HealthB",[90,window.get_size()[1]-115],48,self.colours[0],self.target),
            "BOTTOMarmor": Text("ArmorB",[350,window.get_size()[1]-115],48,self.colours[1],self.target),
            "BOTTOMmana": Text("ManaB",[window.get_size()[0]-75,window.get_size()[0]-380],48,self.colours[2],self.target),

            "Winner": Text("Match",(25,100),50,(255,255,255),self.target,False),
            "Back": Button("Back",[25,200],50,50,24,self.target,False,[[self.updateScores,[]],[self.camera.changeToScene,["Main Menu"]]]),

            #Card("YEDUASDSDAHJSDAhujS","TADS","ASD",3,2,2,[133,200,24],self.target,[200,200],None)'''
        }
        self.table = [
            #Player 1
            [self.getSlot(),self.getSlot(),self.getSlot(),self.getSlot(),self.getSlot()],
            #Player 2
            [self.getSlot(),self.getSlot(),self.getSlot(),self.getSlot(),self.getSlot()]
        ]
        self.UI["Winner"].visible = False
        self.UI["Back"].visible = False

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
        self.drawCard(self.players[0],3)
        self.drawCard(self.players[1],3)
        self.camera.addObject(self.target,self)


    def event(self,event):
        for card in self.table[0]:
            card.event(event)

        for card in self.table[1]:
            card.event(event)
        
        for card in self.players[0].hand:
            card.event(event)
            
        pass

    def updateScores(self):
        if not self.winner == None:
            self.HS.addScore(self.winner,1)

        
    def destory(self):
        for item in self.UI:
            self.UI[item].destory()
        
        Cards.cardlist = []
        self.camera.cleanScene("Game")
        self.camera.destoryScene("Game")
        del self
    
    def drawTable(self):
        nextCardPosition = 0
        i = 0
        for card in self.table[0]:
            len(self.table)
            if card == None:
                pass
            else:
                card.pos = [75+nextCardPosition,190]
                card.scale = 0.25
                card.changeVisibility(True)
                card.update()
                card.draw()
                
                if card.health <= 0:
                    self.table[0][i] = self.getSlot()
                if not self.selectedUnit == None:
                    if not self.selectedCard:
                        
                        if type(card).__name__ == "Slot":
                            card.active = False
                        else:
                            card.active = True

                        if card.selected:
                            if not type(card).__name__ == "Slot":
                                self.targetUnit = card
                                self.attack(self.targetUnit,self.selectedUnit)
                else:
                    card.active = False
            
            i += 1
            nextCardPosition += 131
        
        nextCardPosition = 0
        i = 0
        
        # Playing player cards
        for card in self.table[1]:
            if card == None:
                pass
            else:
                card.pos = [75+nextCardPosition,411]
                card.scale = 0.25
                card.changeVisibility(True)
                card.update()
                card.draw()
                if card.health <= 0:
                    self.table[1][i] = self.getSlot()

                if type(card).__name__ == "Slot":
                    card.active = True

                if card.selected:
                    if not type(card).__name__ == "Slot":
                        self.selectedUnit = card
                    else:
                        if self.selectedCard:
                            self.playCard(i)
                            self.selectedCard = False

                try:
                    self.selectedUnit.isSelected = True
                except:
                    pass
                
            i += 1
            nextCardPosition += 131

        if not self.selectedUnit == None:
            self.UI["TOPplayer"].action = [[self.attack,[self.players[1],self.selectedUnit]]]
            self.UI["BOTTOMplayer"].action = [[self.attack,[self.players[0],self.selectedUnit]]]
        else:
            self.UI["TOPplayer"].action = None
            self.UI["BOTTOMplayer"].action = None

    def drawHands(self):
        #print(self.players[0].hand)
        nextCardPosition = 0
        for card in self.players[0].hand:
            if card == None:
                pass
            else:
                card.pos = [self.window.get_size()[0]-490+nextCardPosition,self.window.get_size()[1]-(card.size[1]*card.scale)]
                card.scale = 0.2
                card.changeVisibility(True)
                card.update()
                card.draw()
                if card.selected:
                    self.selectedCard = True
                    self.selectedUnit = card
                try:
                    self.selectedUnit.isSelected = True
                except:
                    pass
            if card.cost <= self.players[0].mana:
                card.active = True
            else:
                card.active = False
            nextCardPosition += 100
        pass

    def updateUI(self):
        self.UI["TurnCounter"].Text("Turn: "+str(self.turn[0]))
        self.UI["CurrentPlayer"].Text("Playing: " + str(self.players[0].name))

        self.UI["TOPplayer"].Text(self.players[1].name)
        self.UI["TOPhealth"].Text(str(self.players[1].health))
        self.UI["TOParmor"].Text(str(self.players[1].armor))
        self.UI["TOPmana"].Text(str(self.players[1].mana) + "/" + str(self.players[1].currentMaxMana))

        self.UI["BOTTOMplayer"].Text(self.players[0].name)
        self.UI["BOTTOMhealth"].Text(str(self.players[0].health))
        self.UI["BOTTOMarmor"].Text(str(self.players[0].armor))
        self.UI["BOTTOMmana"].Text(str(self.players[0].mana) + "/" + str(self.players[0].currentMaxMana))

    def update(self):
        if self.gameloop:
            #pygame.draw.rect(self.camera.surface,(100,100,100),self.board) #self.camera.surface.blit(self.board,(0,0))
            pygame.draw.rect(self.camera.surface,(100,100,100),(50,0,450,150))
            pygame.draw.rect(self.camera.surface,(100,100,100),(self.window.get_size()[0]-500,self.window.get_size()[1]-150,450,150))
            self.drawTable()
            self.drawHands()
        self.updateUI()
        self.endgame(self.players)
    
    # just needs to exist so camera.py doesn't throw an error
    def draw(self):
        pass

    def endgame(self,player):
        end = False

        if player[0].health <= 0 and player[1].health <= 0:
            end = True
            self.UI["Winner"].Text("Match - Draw")
            for item in self.UI:
                self.UI[item].changeVisibility(False)
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
            
            self.UI["Winner"].changeVisibility(True)

        elif player[0].health <= 0:
            end = True
            self.UI["Winner"].Text("Match - Winner: " + player[1].name)
            self.winner = player[1].name

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
            self.UI["Winner"].Text("Match - Winner: " + player[0].name)
            self.winner = player[0].name

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
            self.gameloop = False
            self.UI["Winner"].visible = True
            self.UI["Back"].visible = True

    def attack(self,target,attacker):
        target.health -= attacker.attack
        attacker.health -= target.attack
        attacker.active = False
        self.selectedUnit = None
        self.targetUnit = None
        
    def changeTurn(self):
        if self.turn[1] == 1:
            self.turn[1] = 0
        else:
            self.turn[1] = 1
        
        self.players[1].currentMaxMana += 1

        if self.players[1].currentMaxMana >= self.players[1].maxMana:
            self.players[1].currentMaxMana = self.players[1].maxMana

        self.players[1].mana = self.players[1].currentMaxMana

        # Player index 0 now has a go!
        temp = self.players[0]
        self.players[0] = self.players[1]
        self.players[1] = temp

        temp = self.UI["TOPplayer"].action
        self.UI["TOPplayer"].action = self.UI["BOTTOMplayer"].action
        self.UI["BOTTOMplayer"].action = temp

        temp = self.table[0]
        self.table[0] = self.table[1]
        self.table[1] = temp

        self.selectedCard = False
        self.selectedUnit = None

        self.drawCard(self.players[0],1)

        self.turn[0] += 1

        # Activate Player Cards
        for card in self.table[1]:
            if card == None:
                pass
            else:
                card.active = True

    def getCard(self,position):
        temp = Cards.cardlist[position]
        card = Champion(temp.name,temp.image,temp.title,temp.description,temp.attack,temp.health,temp.cost,temp.pos)
        return card
    
    def getSlot(self):
        slot = Slot()
        return slot

    def drawCard(self,target,amount=1,type=-1):
        for x in range(0,amount):
            if (len(target.hand)+1 <= 4):
                y = randint(0,len(target.deck)-1)
                target.deck[y][1] -= 1
                target.hand.append(copy.copy(target.deck[y][0]))
            else:
                y = randint(0,len(target.deck)-1)
                target.deck[y][1] -= 1
        
        if (target.deck[y][1] <= 0):
            del target.deck[y]
            

    def summonCard(self,entity,amount=1,location=-1):
        # Summons a card
        for x in range(0,amount):
            #print("Summoned - ",entity.name)
            self.table[self.turn[1]].append(entity)

    def playCard(self,position):
        self.players[0].mana -= self.selectedUnit.cost
        self.selectedUnit.active = False
        self.table[1][position] = self.selectedUnit
        i = -1
        for item in range(0,len(self.players[0].hand)):
            print(item)
            if self.players[0].hand[i] == self.selectedUnit:
                del self.players[0].hand[i]
            i += 1
        del self.selectedUnit
        self.selectedUnit = None
		
    def destoryCard(self,card):
        del card

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