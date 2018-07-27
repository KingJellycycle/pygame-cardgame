from cardgame import *
from player import *

table = [
    #Player 1
    [],
    #Player 2
    []
]

cardgame = cardgame()
playerone = player("Player1",cardgame.getStandard())
playertwo = player("Player2",cardgame.getStandard())
turn = [0,0]


def load():
    pass


def update():
    print("Main Initialising")
    print("=================")
    while (playerone.health > 1 or playertwo.health > 1):
        turn[0] += 1

        if (turn[1] == 0):
            PlayPhase(playerone,table,0)
            turn[1] = 1

        if (turn[1] == 1):
            
            PlayPhase(playertwo,table,1)
            turn[1] = 0


def PlayPhase(player,table,i):
    print("Summon Phase")
    print("============")
    print("Player Hand: ",player.name)
    print(decode(player.hand))
    print(player.hand)
    print("=================")
    print("Your side:")
    print(decode(table[i]))
    print("=================")
    print("Enemy side:")
    cardgame.Summon(table,cardgame.cards[1][0])
    if (i == 1):
        print(decode(table[0]))
    else:
        print(decode(table[1]))
        
    player.play(int(input()),table[i])
    AttackPhase(player,table,i)

def AttackPhase(player,table,i):
    print("=======")
    print("Attack Phase")
    print("=======")
    input()
    SwitchPhase(player,table,i)
    pass

def SwitchPhase(player,table,i):
    print("=======")
    print("Switch Phase")
    print("=======")
    input()
    pass

def decode(array):
    temp = []
    for x in range(0,len(array)):
        temp.append(cardgame.cards[array[x][0]][array[x][1]][0])

    return temp