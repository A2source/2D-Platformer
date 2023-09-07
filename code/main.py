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
    
    player = Player(Controller(), player_controls, 0, 150, 8, 8, init_speed=0, init_accel=0.007, init_decel=0.004, max_speed=3.5, jump_speed=0.05, jump_height=700, colour=[255, 255, 255])
    
    prevT = framerate.get_time()

    running = True
    while(running):
        framerate.tick_busy_loop(fps)
        t = framerate.get_time()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
                
        DISPLAYSURF.fill(0)

        player.update(DISPLAYSURF, events, t)
        
        pygame.display.flip()
        
def exit():
    
    # quit everything
    pygame.quit()
    sys.exit()

if __name__ == '__main__': main()