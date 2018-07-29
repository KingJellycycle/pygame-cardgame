import pygame
from cardgame import *
from player import *

cardgame = cardgame()
playerone = player("Player1",cardgame.getStandard())
playertwo = player("Player2",cardgame.getStandard())
cardgame.turn = [0,0]

def draw(surface):
    pygame.draw.rect(surface, [185,80,0], [0,0,surface.get_width(),surface.get_height()/2-50])
    pygame.draw.rect(surface, [185,80,0], [0,surface.get_height()/2,surface.get_width(),surface.get_height()/2])
    pygame.draw.rect(surface, [100,100,100], [0,surface.get_height()/2-50,surface.get_width(),50])

    pass

def update():
    pass