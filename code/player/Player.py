import pygame
import sys

class Player():
    
    def __init__(self, controller, controls, x, y, w, h, init_speed, init_accel, init_momentum, max_momentum, colour):
        
        self.controller = controller
        self.controls = controls
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.speed = init_speed
        self.accel = init_accel
        self.momentum = init_momentum
        
        self.max_momentum = max_momentum
        
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
        
        prev_x = self.x
        
        self.controller.update(events)
        
        self.moving = False
        
        keys = self.controller.holding
        if contains(keys, self.controls['left']) or contains(keys, self.controls['right']) or contains(keys, self.controls['down']):
            self.moving = True
            
        if self.moving:
            self.momentum += (self.accel + (prev_x - self.x)) / 50
            
        if not self.moving and self.momentum > 0:
            self.momentum -= (self.speed * self.accel) / 2
            
        if self.momentum > self.max_momentum:
            self.momentum = self.max_momentum
            
        if contains(keys, self.controls['left']):
            self.x -= self.speed * self.momentum
            
        if contains(keys, self.controls['right']):
            self.x += self.speed * self.momentum
            
        # self.y -= (self.accel * self.speed) - 40
        
        if self.momentum < 0:
            self.momentum = 0
            
        if self.x < 0:
            self.x = 250
            
        if self.x > 250:
            self.x = 0

#######################################################
        
def contains(check_list, elements):
    if type(elements) == list:
        for e in elements:
            count = check_list.count(e)
            
            if count > 0:
                return count
            
    else:
        return check_list.count(elements) > 0