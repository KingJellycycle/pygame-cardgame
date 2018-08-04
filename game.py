import pygame
from cardgame import *
from camera import *
from UI import *
#from player import *

cardgame = cardgame()

GS = 0
Phase = "Summon"

bg = pygame.image.load("./assets/images/board.png")
bgrect = bg.get_rect()

def draw(surface):
    global GS
    # Draw Board
    if (GS == 0):
        # Menu

        GS = 1
    
    if (GS == 1):
        # Game


        # BG
        surface.blit(bg, bgrect)
        if (Phase == "Summon"):
            # Draw Cards
            cardgame.draw(surface)
        
        if (Phase == "Attack"):
            pass
        
        if (Phase == "Swap"):
            turn[0] += 1
            if turn[1] == 1:
                turn[1] = 0
            else:
                turn[1] = 1

    pygame.display.flip()
    pass

def update():
    pass
