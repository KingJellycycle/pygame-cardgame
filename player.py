from random import randint

class player:
    
    def __init__(self,name,deck,flag=[30,0,0]):
        self.name = name
        self.deck = deck

        self.health = flag[0]
        self.armor = flag[1]
        self.attack = flag[2]
        
        self.hand = []
        self.draw(5)
        print(self.hand)

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
        