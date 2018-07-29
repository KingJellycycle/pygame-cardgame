from cardgame import *
from player import *

cardgame = cardgame()
playerone = player("Player1",cardgame.getStandard())
playertwo = player("Player2",cardgame.getStandard())
cardgame.turn = [0,0]


def load():
    pass

def draw():
    
    pass

def update():
    print("Main Initialising")
    print("=================")
    while (playerone.health > 1 or playertwo.health > 1):
        cardgame.turn[0] += 1

        if (cardgame.turn[1] == 0):
            PlayPhase(playerone,0)
            cardgame.turn[1] = 1

        if (cardgame.turn[1] == 1):
            
            PlayPhase(playertwo,1)
            cardgame.turn[1] = 0


def PlayPhase(player,i):
    print("Summon Phase")
    print("============")
    print("Player Hand: ",player.name)
    print(cardgame.decode(player.hand))
    print(player.hand)
    print("=================")
    print("Your side:")
    print(cardgame.decode(cardgame.table[i]))
    print("=================")
    print("Enemy side:")
    if (i == 1):
        print(cardgame.decode(cardgame.table[0]))
    else:
        print(cardgame.decode(cardgame.table[1]))
    player.play(int(input()),cardgame.table[i])
    AttackPhase(player,i)

def AttackPhase(player,i):
    print("=======")
    print("Attack Phase")
    print("=======")
    #input()
    SwitchPhase(player,i)
    pass

def SwitchPhase(player,i):
    print("=======")
    print("Switch Phase")
    print("=======")
    #input()
    pass