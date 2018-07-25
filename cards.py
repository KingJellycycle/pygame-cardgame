class cards:

    def __init__(self):
        # Cards will work like this
        # Type - Name, Description, Cost, Action (Function)
        print("Initialising cards and various other setup things!")

        self.cards = [
            # Spells
            [
                ["Attack", "Attack", 2],
                ["Taunt", "Makes a unit into a taunt",3],
                ["Heal", "Heals Who ever is picked",1]
            ],
            # Units
            [
                ["Monster1","Default Monster",1],
                ["Monster2","Default Monster",1],
                ["Monster3","Default Monster",1],
                ["Monster4","Default Monster",1]
            ],
            #Secrets
            [
                ["Damage Nullifier","Don't take next hit! (Last 1 Turn)",4]
            ]
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
