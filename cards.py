class cards:

    def __init__(self):
        # Cards will work like this
        # Type - Name, Description, Cost, Action (Function)
        print("Setting up cards!")

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
                ["Monster4","Default Monster",1],
            ],
            #Secrets
            [
                ["Damage Nullifier","Don't take next hit! (Last 1 Turn)",4]
            ]
        ]

    def getStandard(self):
        return [
            # Spells
            [
                ["Attack", 2],
                ["Taunt",3],
                ["Heal", 1]
            ],
            # Units
            [
                ["Monster1",1],
                ["Monster2",1],
                ["Monster3",1],
                ["Monster4",1],
            ],
            #Secrets
            [
                ["Damage Nullifier",4]
            ]
        ]

    def deal(self):
        return 0
