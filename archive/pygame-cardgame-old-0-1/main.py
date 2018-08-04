import pygame 
import game

pygame.init()

pygame.display.set_caption('R')
clock = pygame.time.Clock()
fps = 60

gameDisp = pygame.display.set_mode((800, 600), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

def quitfunc():
    pygame.quit()
    quit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitfunc()

    game.update()
    game.draw()

    pygame.display.update()
    clock.tick(fps)

pygame.quit()