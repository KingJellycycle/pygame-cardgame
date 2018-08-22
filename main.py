#import pygame 
from game import *


settings = [
    # Title
    "Hexwars",
    # Volumes (If i even have sounds)
    [],
    # Misc
    []
]

screenSize = [1024,768]

pygame.init()
pygame.font.init()
pygame.display.set_caption(settings[0])
clock = pygame.time.Clock()
fps = 60

window = pygame.display.set_mode((screenSize), pygame.HWSURFACE|pygame.DOUBLEBUF)

# Dim Menu
#s = pygame.Surface(screenSize)
#s.set_alpha(200)
#s.fill((25,25,25))

Camera = Camera([0,0],screenSize)

Camera.newScene("Main Menu",[],0,True)
Camera.newScene("Game",[],1,False)
Camera.newScene("Deck Builder",[],2,False)
Camera.newScene("Pause",[],5,False)

#Camera.addObject("Main Menu",[text3,textrect3])

UI = UI(Camera)
#UI.createText("YE",24,"Main Menu",[500,500])

MenuText = Text(settings[0],64,(200,200,200),"Main Menu",[screenSize[0]/2,50])
PlayButton = Button("Play",[250,100,24],"Main Menu",[screenSize[0]/2-100,200],"UI.camera.changeToScene('Game')")
ExitButton = Button("Exit",[250,100,24],"Main Menu",[screenSize[0]/2-100,350],"pygame.quit()")
#Button = Button("Test",[2,2,2],"Main Menu",[50,50])
game = Game(window)
Camera.addObject("Game",game)

gameClock = 0

gameTick = 0

def quitfunc():
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitfunc()

    # Global tick count + seconds passed
    gameTick += 1

    if gameTick % (fps / 1) == 0:
        gameClock += 1

    # Updates
    #update()

    # Draws

    Camera.update(window)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()