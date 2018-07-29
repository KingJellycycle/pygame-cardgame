import pygame
from cardgame import *
from player import *

cardgame = cardgame()
playerone = player("Player1",cardgame.getStandard())
playertwo = player("Player2",cardgame.getStandard())

GS = 0

bg = pygame.image.load("./assets/images/board.png")
bgrect = bg.get_rect()

def draw(surface):
    global GS
    # Draw Board
    if (GS == 0):
        # Menu
        surface.fill([255,255,255])
        GS = 1
    
    if (GS == 1):
        # Game
        surface.fill([255,255,255])

        # BG
        surface.blit(bg, bgrect)
        
        # Draw Cards
        print(card.cardlist[0].pos)

        # Player one cards
        card.cardlist[0].pos[0] = card.cardlocation[2][0]
        card.cardlist[1].pos[0] = card.cardlocation[2][1]
        card.cardlist[2].pos[0] = card.cardlocation[2][2]
        card.cardlist[3].pos[0] = card.cardlocation[2][3]

        # Player two cards
        card.cardlist[0].pos[1] = card.cardlocation[0][0]
        card.cardlist[1].pos[1] = card.cardlocation[0][1]
        card.cardlist[2].pos[1] = card.cardlocation[0][2]
        card.cardlist[3].pos[1] = card.cardlocation[0][3]

        card.draw(surface,0)
        card.draw(surface,1)

    pygame.display.flip()
    pass

def update():
    pass