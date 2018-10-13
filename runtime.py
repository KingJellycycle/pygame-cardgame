import pygame 
from game import *
from camera import *
from UI import *
from highscore import *

settings = [
    # Title
    "Hexwar",
    [1024,768],
    # Volumes (If i even have sounds)
    [],
    # Misc
    []
]

pygame.init()
pygame.font.init()
pygame.display.set_caption(settings[0])

clock = pygame.time.Clock()
fps = 60

window = pygame.display.set_mode((settings[1]), pygame.HWSURFACE|pygame.DOUBLEBUF)
window.set_alpha(None)

camera = Camera([0,0],settings[1])

camera.newScene("Main Menu",[],0,True)
camera.newScene("Game",[],1,False)
camera.newScene("Deck Builder",[],2,False)
camera.newScene("Pause",[],5,False)

UI.camera = camera

HS = HSsystem()
scoreList = HS.getScores(5)

def createGame(window,camera):
    global game
    try: 
        game.destory()
        print("Game Destoryed!")
    except NameError: 
        pass
    print("runtime.py - Creating a new Game!")
    cardInit(camera)
    game = Game(window,camera,[menu["InputP1"].text],[menu["InputP2"].text],HS)
    print("runtime.py - New Game created!")


def quitfunc(window):
    gameRunning = False
    HS.saveScores()
    camera.destory(window)
    pygame.font.quit()
    pygame.display.quit()
    pygame.quit()


menu = {
    
    "Title": Text(settings[0],[settings[1][0]/2,50],64,(200,200,200),"Main Menu",True),
    #text,pos,width,height,size,target,action=None,colour=[UI.theme[1],UI.theme[2],UI.theme[3]],layer=None
    "Play": Button("Play",[settings[1][0]/2-100,200],250,100,24,"Main Menu",False,[[createGame,[window,camera]],[camera.changeToScene,['Game']]]),
    "Exit": Button("Exit",[settings[1][0]/2-100,350],250,100,24,"Main Menu",False,[[quitfunc,[window]]]),
    "HighscoreBG": Panel([settings[1][0]-300,0],300,225,"Main Menu",False,(150,150,150)),
    "HStitle": Text("Highscores (WINS):",[settings[1][0]-295,5],35,(255,255,255),"Main Menu",False),
    "HS1": Text("1: ",[settings[1][0]-285,40],24,(255,255,255),"Main Menu",False),
    "HS2": Text("2: ",[settings[1][0]-285,80],24,(255,255,255),"Main Menu",False),
    "HS3": Text("3: ",[settings[1][0]-285,120],24,(255,255,255),"Main Menu",False),
    "HS4": Text("4: ",[settings[1][0]-285,160],24,(255,255,255),"Main Menu",False),
    "HS5": Text("5: ",[settings[1][0]-285,200],24,(255,255,255),"Main Menu",False),

    "TextPlayers": Text("Please input player names!",[50,250],32,(255,255,255),"Main Menu",False),
    "TextP1": Text("Player One!",[50,275],32,(255,255,255),"Main Menu",False),
    "TextP2": Text("Player Two!",[50,350],32,(255,255,255),"Main Menu",False),
    "InputP1": Input([50,300],[100,25],"Main Menu"),
    "InputP2": Input([50,375],[100,25],"Main Menu"),
}

gameTick = 0
FPSFont = pygame.font.Font("./assets/font/font.ttf",24)
gameRunning = True

while gameRunning:
    
    for event in pygame.event.get():
        camera.event(event)
        if event.type == pygame.QUIT:
            quitfunc(window)

    if gameTick % (fps) == 0:
        scoreList = HS.getScores(5)
        for i in range(0, len(scoreList)):
            menu["HS"+str(i+1)].Text(str(i+1) + ": " + str(scoreList[i][0]) + " - " + str(scoreList[i][1]) + " - " + str(scoreList[i][2]))

    gameTick += 1
    camera.update(window)

    # FPS DISPLAY
    FPS_OVERLAY = FPSFont.render(str(round(clock.get_fps(),0)), True, (255,255,255))
    window.blit(FPS_OVERLAY,(0,0))

    # Refresh the window
    pygame.display.update()
    clock.tick(fps)

pygame.quit()