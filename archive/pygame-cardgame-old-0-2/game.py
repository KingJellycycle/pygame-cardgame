import pygame
from cardgame import *
from player import *

cardgame = cardgame()
playerone = player("Player1",cardgame.getStandard())
playertwo = player("Player2",cardgame.getStandard())

GS = 0
Phase = "Summon"

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
        if (Phase == "Summon"):
            # Draw Cards

            #playerone.deck[0].pos[0] = card.cardlocation[0][3]
            card.draw(surface,0)
            card.draw(surface,1)
        
        if (Phase == "Attack"):
            pass
        
        if (Phase == "Swap"):
            pass

    pygame.display.flip()
    pass

def update():
    pass