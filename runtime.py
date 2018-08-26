import pygame 
import main
import importlib

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

def quitfunc():
    pygame.display.quit()
    pygame.quit()
    quit()

main.init(screenSize,settings,window,quitfunc)

gameClock = 0

gameTick = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitfunc()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                    print("Reloading Game!")
                    print("===============")
                    print("Destorying all Instances!")
                    main.destroy()
                    print("Reloading Game File!")
                    importlib.reload(main)
                    #importlib.reload(Game)
                    print("Creating Game!")
                    main.init(screenSize,settings,window,quitfunc)
    
    gameTick += 1
    main.update(window)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()