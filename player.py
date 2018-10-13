from random import randint

# Set variables that's all
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