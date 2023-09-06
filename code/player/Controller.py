import pygame

class Controller:

    def __init__(self):
        self.holding = []

    def update(self, events):
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                
                key = event.unicode
                if event.unicode == '':
                    key = event.key
                    
                self.holding.insert(event.key, key)
                
            elif event.type == pygame.KEYUP:
            
                key = event.unicode
                if event.unicode == '':
                    key = event.key
                    
                self.holding.remove(key)