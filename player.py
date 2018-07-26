from random import randint

class player:
    
    def __init__(self,name,deck,flag=[30,0,0]):
        self.name = name
        self.deck = deck

        self.health = flag[0]
        self.armor = flag[1]
        self.attack = flag[2]
        
        self.hand = self.draw(5)

    def draw(self, amount, type=-1):
        temptable = []
        for x in range(0,amount):
            print("X - ",x," Amount - ",amount)
            y = randint(0,len(self.deck)-1)
            print("=======")
            print("Y - ",x)
            print(y)
            print("=======")
            self.deck[y][2] -= 1
            if (self.deck[y][2] == 0):
                del self.deck[y]

            temptable.append([self.deck[y][0],self.deck[y][1]])
            
        return temptable

    def play(self, cardno, side):
        print(self.hand[cardno])
        side.append(self.hand[cardno])
        del self.hand[cardno]
        