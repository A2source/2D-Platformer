import pygame
import sys

class Player():
    
    def __init__(self, controller, controls, x, y, w, h, init_speed, init_accel, init_decel, max_speed, jump_speed, jump_height, colour):
        
        self.controller = controller
        self.controls = controls
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        # create velocity vector
        self.velocity = [0, 0]
        
        self.speed = init_speed
        self.accel = init_accel
        self.decel = init_decel
        
        self.max_speed = max_speed
        
        self.colour = pygame.Color(colour[0], colour[1], colour[2])
        
        print('\n## Created Player ##')
        print(f'X: {x} | Y: {y} | W: {w} | H: {h}')
        print(f'Speed: {self.speed} | Accel: {self.accel}')
        print(f'Colour: {self.colour}\n')
        
        self.moving = False
        
        self.jumping = False
        self.falling = False
        self.grounded = True
        
        self.jump_speed = jump_speed
        self.max_jump_height = jump_height
        
        self.init_jump_y = self.y
        self.cur_jump_height = 0
        
    def draw(self, surf):
        pygame.draw.rect(surf, self.colour, ((self.x, self.y), (self.w, self.h)))
        
    def update(self, surf, events, dt):
        self.draw(surf)
        
        prev_x = self.x
        
        self.controller.update(events)
        
        self.moving = False
        
        keys = self.controller.holding
        if contains(keys, self.controls['left']) or contains(keys, self.controls['right']) or contains(keys, self.controls['down']):
            self.moving = True
        
        # https://www.instructables.com/Advanced-Platformer-Movement/
        # THE GOAT RIGHT HERE
        
        if contains(keys, self.controls['left']):
            self.velocity[0] -= (self.max_speed * self.accel * dt)
            
        if contains(keys, self.controls['right']):
            self.velocity[0] += (self.max_speed * self.accel * dt)
            
        if not contains(keys, self.controls['left']) and not contains(keys, self.controls['right']):
            if self.velocity[0] < 0:
                self.velocity[0] += (self.decel * self.max_speed * dt)
                
                if self.velocity[0] > 0:
                    self.velocity[0] = 0

            elif self.velocity[0] > 0:
                self.velocity[0] -= (self.decel * self.max_speed * dt)
                
                if self.velocity[0] < 0:
                    self.velocity[0] = 0
                    
        if contains(keys, self.controls['jump']) and self.grounded and self.cur_jump_height < self.max_jump_height:
            self.grounded = False
            self.jumping = True
            
            self.velocity[1] = -self.jump_speed
            
            self.velocity[1] += (self.jump_speed * self.accel * dt)
            self.init_jump_y = self.y
            
        if self.jumping:
            self.cur_jump_height -= self.y - self.init_jump_y
            
        print(self.cur_jump_height)
            
        if not contains(keys, self.controls['jump']) and self.jumping or self.cur_jump_height > self.max_jump_height:
            
            if not self.falling:
                self.velocity[1] = self.jump_speed
                
            else:
                self.velocity[1] += easeInQuint((-self.jump_speed * self.accel * dt))
            
            self.falling = True

            if self.y >= 150:
                self.grounded = True
                self.jumping = False
                self.falling = False
                
                self.velocity[1] = 0
                self.cur_jump_height = 0
        
        self.velocity[0] = clamp(self.velocity[0], -self.max_speed, self.max_speed)
        self.velocity[1] = clamp(easeOutQuint(self.velocity[1]), -self.max_speed, self.max_speed)
        
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        
        #print(self.velocity)
            
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
        
def clamp(value, lower, upper):
    if value > upper:
        return upper
    
    if value < lower:
        return lower
   
    return value

def easeInQuint(t):
    return t * t * t * t * t
    
def easeOutQuint(t):
    t -= 1
    return t * t * t * t * t + 1