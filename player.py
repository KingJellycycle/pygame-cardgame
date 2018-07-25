class player:
    
    def __init__(self,name,deck,flag=[30,0,0]):
        self.name = name
        self.deck = deck

        self.health = flag[0]
        self.armor = flag[1]
        self.attack = flag[2]
        
        self.hand = self.draw(5)

    def draw(self, amount, type=-1):
        pass

    def play(self, cardno):
        hand

    