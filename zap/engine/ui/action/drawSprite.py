import pygame

class DrawSprite:
    def __init__(self, group):
        self.group = group
        self.ctr = 0
        self.name = "draw_sprite_action"
        self.types = ["display"]
        self.children = []
        self.entity_state = None
        self.verbose = False
        return
    
    def condition_to_act(self, draw_screen_data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if draw_screen_data == None:
            return False
        return True
    
    def act(self, draw_screen_data):
        if self.condition_to_act(draw_screen_data):
            self.drawSprite(draw_screen_data)
    
    def drawSprite(self, draw_screen_data):
        while self.ctr != self.entity_state.timeUntil:
            self.ctr+=1
        self.group.add(self.entity_state)
        self.group.draw(draw_screen_data)
