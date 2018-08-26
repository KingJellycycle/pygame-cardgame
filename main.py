#import pygame 
from game import *

def init(screenSize,settings,window,quitfunc):
    global Camera
    global UI
    global elements
    Camera = Camera([0,0],screenSize)
    Camera.newScene("Main Menu",[],0,True)
    Camera.newScene("Game",[],1,False)
    Camera.newScene("Deck Builder",[],2,False)
    Camera.newScene("Pause",[],5,False)

    UI = UI(Camera)

    elements = [
        Text(settings[0],64,(200,200,200),"Main Menu",[screenSize[0]/2,50]),
        Button("Play",[250,100,24],"Main Menu",[screenSize[0]/2-100,200],[[createGame,[window,Camera]],[Camera.changeToScene,['Game']]]),
        Button("Exit",[250,100,24],"Main Menu",[screenSize[0]/2-100,350],[[quitfunc,[]]])
    ]
    print("main.py - Init")

def destroy():
    global Camera
    global UI
    global elements
    del elements
    del Camera
    del UI
    pass
    
def createGame(window,camera):
    global game
    try: 
        game.destory()
        print("Game Destoryed!")
    except NameError: 
        pass
    print("main.py - Creating a new Game!")
    cardInit()
    game = Game(window,camera)
    print("main.py - New Game created!")
    
def update(window):
    Camera.update(window)
    #print(Camera.Scenes)

    