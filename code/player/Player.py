import pygame
import sys

class Player():
    
    def __init__(self, controller, controls, x, y, w, h, init_speed, init_accel, init_momentum, colour):
        
        self.controller = controller
        self.controls = controls
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.speed = init_speed
        self.accel = init_accel
        self.momentum = init_momentum
        
        self.colour = pygame.Color(colour[0], colour[1], colour[2])
        
        print('\n## Created Player ##')
        print(f'X: {x} | Y: {y} | W: {w} | H: {h}')
        print(f'Speed: {self.speed} | Accel: {self.accel} | Momentum: {self.momentum}')
        print(f'Colour: {self.colour}\n')
        
        self.moving = False
        
    def draw(self, surf):
        pygame.draw.rect(surf, self.colour, ((self.x, self.y), (self.w, self.h)))
        
    def update(self, surf, events):
        self.draw(surf)
        
        self.controller.update(events)
        
        self.moving = False
        
        keys = self.controller.holding
        if contains(keys, self.controls['left']) or contains(keys, self.controls['right']) or contains(keys, self.controls['down']):
            self.moving = True
            
        if contains(keys, self.controls['left']):
            self.x -= self.speed
            
        if contains(keys, self.controls['right']):
            self.x += self.speed
        
def contains(check_list, elements):
    if type(elements) == list:
        for e in elements:
            count = check_list.count(e)
            
            if count > 0:
                return count
            
    else:
        return check_list.count(elements) > 0