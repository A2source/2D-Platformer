import os, sys
import pygame

from player.Controller import *
from player.Player import *

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

GAME_RECT = pygame.Rect(0, 0, 256, 240)
DISPLAYSURF = pygame.display.set_mode((256, 240), pygame.SRCALPHA | pygame.SCALED, 32)

framerate = pygame.time.Clock()

def main():

    fps = 60
    
    player_controls = {'left': ['a', 1073741904], 'jump': ['w', ' ', 1073741906], 'down': ['s', 1073741905], 'right': ['d', 1073741903]}
    
    player = Player(Controller(), player_controls, 0, 0, 8, 8, 5, 5, 5, [255, 255, 255])
    
    running = True
    while(running):
        framerate.tick_busy_loop(fps)
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
                
        DISPLAYSURF.fill(0)

        player.update(DISPLAYSURF, events)
        
        pygame.display.flip()
        
def exit():
    
    # quit everything
    pygame.quit()
    sys.exit()

if __name__ == '__main__': main()