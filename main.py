#import pygame 
from game import *

global settings
settings = [
    # Title
    "Piltover's Treasury",
    # Volumes (If i even have sounds)
    [],
    # Misc
    []
]

global screenSize
screenSize = [1024,768]

pygame.init()

pygame.display.set_caption(settings[0])
clock = pygame.time.Clock()
fps = 60

gameDisp = pygame.display.set_mode((screenSize), pygame.HWSURFACE|pygame.DOUBLEBUF)

# Dim Menu
#s = pygame.Surface(screenSize)
#s.set_alpha(200)
#s.fill((25,25,25))

Camera = Camera(gameDisp,[0,0],screenSize)

Camera.newScene("Main Menu",[],0,True)
Camera.newScene("Game",[],1,False)
Camera.newScene("Deck Builder",[],2,False)
Camera.newScene("Pause",[],5,False)

#Camera.addObject("Main Menu",[text3,textrect3])

UI = UI(Camera)
UI.createText("YE",24,"Main Menu",[500,500],0)
UI.createText("YE2",24,"Main Menu",[500,550],0)

global gameClock
gameClock = 0

gameTick = 0

def quitfunc():
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitfunc()

    # WIll use this later
    gameTick += 1

    if gameTick % (fps / 1) == 0:
        gameClock += 1
    
    # Draws
    Camera.draw()
    # Updates
    #pygame.draw.rect(gameDisp, (100,100,100), [400,300,100,100])
    update()
    
    # DIMMER BUT WILL ALWAYS BE ON TOP OF CAM :/
    #gameDisp.blit(s, (0,0))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()