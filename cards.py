class cards:

    def __init__(self):
        # Cards will work like this
        # Type - Name, Description, Amount, Action (Function)
        print("Setting up cards!")

        self.deck = [
            # Spells
            [
                ["Attack", "Attack"],
                ["Taunt", "Makes a unit into a taunt"],
                ["Heal", "Heals Who ever is picked"]
            ],
            # Units
            [
                ["Monster1","Default Monster"],
                ["Monster2","Default Monster"],
                ["Monster3","Default Monster"],
                ["Monster4","Default Monster"],
            ],
            #Secrets
            [
                ["Damage Nullifier","Don't take next hit! (Last 1 Turn)"]
            ]
        ]


    def deal(self):
        return 0
