from cards import *
from player import *

table = [
    #Player 1
    [],
    #Player 2
    []
]

cards = cards()
playerone = player("Player1",cards.getStandard())
playertwo = player("Player2",cards.getStandard())
turn = 0


def load():
    pass


def update():
    print("Main Initialising")
    print("=================")
    while (playerone.health > 1 or playertwo.health > 1):
        turn += 1 
        print("")
        print("Player Hand: ")
        print(playerone.hand)
        print("=================")
        print("")
        print(table)
        playerone.play(int(input()),table)