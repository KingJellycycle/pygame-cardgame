from random import randint

class Player:
    
    def __init__(self,name,deck,health,armor,attack,mana,maxMana):
        self.name = name
        self.deck = deck
        self.health = health
        self.armor = armor
        self.attack = attack
        self.mana = 1
        self.currentMaxMana = 1
        self.maxMana = 10
        self.hand = []

'''
    def draw(self, amount, type=-1):
        for x in range(0,amount):
            if (len(self.hand) <= 6):
                y = randint(0,len(self.deck)-1)
                self.deck[y][1] -= 1
                self.hand.append(self.deck[y][0])
                if (self.deck[y][1] <= 0):
                    del self.deck[y]    
            else:
                y = randint(0,len(self.deck)-1)
                self.deck[y][1] -= 1

                if (self.deck[y][1] <= 0):
                    del self.deck[y]
            
        

    def play(self, cardno, side):
        print(self.hand[cardno])
        side.append(self.hand[cardno])
        del self.hand[cardno]
'''