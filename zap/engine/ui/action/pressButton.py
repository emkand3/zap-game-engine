#####   PRESS BUTTON    #####
#Handles action for pressing your mouse on the button. Type is "event"
import pygame

class PressButton:
    #Constructor
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "press_button_action"
        self.children = []
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, event):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            return self.entity_state.is_inside(pos)
        return False

    #Act: if the action should happen, call all children apart of pressButton's children
    def act(self, event):
        if self.condition_to_act(event):
            for c in self.children:
                c.act()
        return