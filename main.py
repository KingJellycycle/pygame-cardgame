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
    print("Hi")
    print(player.deck[0][1])
    player.play()
    


main()