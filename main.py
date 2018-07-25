from cards import *
from player import *

table = [
    #Player 1
    [],
    #Player 2
    []
]

cards = cards()
player = player("Player1",cards.getStandard())

def main():
    print("Main Initialising")
    print("=================")
    print("")
    print("Player Hand: ")
    print(player.hand)
    print("=================")
    print("")
    player.play(int(input()),table)


    print(table)
    print(player.deck)
    


main()