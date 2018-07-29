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
        # Type - Name, Description, atk, hp, Cost, Action (Function)
        self.cards = [
            # Champions
            [#self.Summon(table,self.cards[0][1])
                ["Azir","Summons 3 soldiers",2,2,3],
                ["Morgana","Nullifies satus effects on unit (pick)",1,3,3],
                ["Ashe","Freeze selected unit",4,1,1],
                ["Jarven IV","Adjacent allies gain 2 atk",2,2,4],
                ["Kindred","Randomly marks a unit on the border, killing this unit gives +3 atk",2,2,4],
                ["Minion (Melee)","Basic Unit",1,3,1],
                ["Super Minion","Basic Unit",3,3,3],
                ["Minion (Caster)","Basic Unit",4,1,2]
            ],
            # Buffs/Potions/Items
            [
                ["Blue Buff","+1 Mana Regen",4],
                ["Red Buff","Applies a debuff for 2 turns (Burn)",4],
                ["Iron Elixer","increase max HP",4]
            ]
        ]

        self.debuffs = [
            ["Burn"]
        ]

    def getStandard(self):
        return [
            # Units
                [0,0,1],
                [0,1,1],
                [0,2,1],
                [0,3,1],
                [0,4,1],
                [0,5,1],
                [0,6,1],
                [0,7,1],
            #Secrets
                [1,0,4],
                [1,1,4],
                [1,2,4] 
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
            temp.append(self.cards[array[x][0]][array[x][1]][0])
        return temp