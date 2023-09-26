#####   DRAW RECTANGLE  #####
#Action for drawing a rectangle. Constructor sets type
#as a "display" type.

import pygame

class DrawRectangleAction:
    #Constructor
    def __init__(self):
        self.name = "draw_rectangle_action"
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, rect_screen_data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if rect_screen_data == None:
            return False
        return True
    
    #Act: if the action is supposed to happen, calls drawR, passing in the screen
    #to be drawn on.
    def act(self, rect_screen_data):
        if self.condition_to_act(rect_screen_data):
            self.drawR(rect_screen_data)
        return
    
    #DrawR: draws the rectangle using pygame's draw.rect method. Uses the Rectangle entity_state
    #that the action is attached to and gets color, coordinates, size, and whether or not it is
    #filled from the entity.
    def drawR(self, surface):
        pygame.draw.rect(surface, self.entity_state.color, pygame.Rect(self.entity_state.coords, self.entity_state.size), self.entity_state.filled)
        for c in self.children:
            c.act()
        return