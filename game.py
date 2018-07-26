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
turn = [0,0]


def load():
    pass


def update():
    print("Main Initialising")
    print("=================")
    while (playerone.health > 1 or playertwo.health > 1):
        turn[0] += 1

        if (turn[1] == 0):
            PlayerPhase(playerone,table,0)
            turn[1] = 1

        if (turn[1] == 1):
            PlayerPhase(playertwo,table,1)
            turn[1] = 0


def PlayerPhase(player,table,i):
    print("Turn: ",turn[0])
    print("Player Hand: ",player.name)
    print(decode(player.hand))
    print(player.hand)
    print("=================")
    print("Your side:")
    print(decode(table[i]))
    print("=================")
    print("Enemy side:")
    if (i == 1):
        print(decode(table[0]))
    else:
        print(decode(table[1]))
        
    player.play(int(input()),table[i])


def decode(array):
    temp = []
    for x in range(0,len(array)):
        temp.append(cards.cards[array[x][0]][array[x][1]][0])

    return temp