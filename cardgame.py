from card import *

class cardgame:

    def __init__(self):
        # Cards will work like this
        print("Initialising cards and various other setup things!")
        
        self.table = [
            #Player 1
            [],
            #Player 2
            []
        ]
        self.turn = [0,0]
        
        self.spells = [                
                ["Heal", "Heals selected Unit",3],
                ["Cleanse", "Removes Status Effects",1],
                ["Snowball", "1 dmg to selected unit",1]
        ]

        self.debuffs = [
            ["Burn"],
            ["Stun"]
        ]

    def getStandard(self):
        return [
            # Units
                [0,2],
                [1,2],
                [2,2],
                [3,4],
                [4,4],
                [5,3]
        ]

    def deal(self):
        return 0

    def summon(self,entity,amount=1,location=-1):
        # location = side of current unit
        for x in range(0,amount):
            print("Summoned - ",self.decode(entity))
            self.table[self.turn[1]].append(entity)
        pass
        
    def decode(self,array):
        temp = []
        for x in range(0,len(array)):
            temp.append(card.cardlist[array[x]].name)
        return temp