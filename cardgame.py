class cardgame:

    def __init__(self):
        # Cards will work like this
        # Type - Name, Description, Cost, Action (Function)
        print("Initialising cards and various other setup things!")
        self.spells = [                
                ["Heal", "Heals selected Unit",3],
                ["Cleanse", "Removes Status Effects",1],
                ["Snowball", "1 dmg to selected unit",1]
        ]
        self.cards = [
            # Summoners Spells
            [],
            # Champions
            [
                ["Azir","Summons 3 soldiers",2,2,1],
                ["Morgana","Nullifies status effects on unit (pick)",1,3,1],
                ["Ashe","Freeze selected unit",4,1,1],
                ["Jarven IV","Adjacent allies gain 2 atk",2,2,1],
                ["Kindred","Randomly marks a unit on the border, killing this unit gives +3 atk",3,2,1],
                ["Minion (Melee)","Basic Unit",1,3,1],
                ["Super Minion","Basic Unit",3,3,1],
                ["Minion (Caster)","Basic Unit",4,1,1]
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
            # Spells
                [0,0,2],
                [0,1,3],
                [0,2,1],
            # Units
                [1,0,1],
                [1,1,1],
                [1,2,1],
                [1,3,1],
            #Secrets
                [2,0,4]
        ]

    def deal(self):
        return 0


    def Summon(self,table,entity,amount=1,location=-1):
        # location = side of current unit
        for x in range(0,amount):
            table.append(entity)
        pass