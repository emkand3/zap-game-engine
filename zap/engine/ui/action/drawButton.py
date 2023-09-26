#####   DRAW BUTTON    #####
#Handles action to draw button. Type set to display. 
import pygame

class DrawButton:
    #Constructor
    def __init__(self):
        self.name = "Draw Button"
        self.types = ["display"]
        self.children = []
        self.entity_state = None
        self.verbose = False
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, button_screen_data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if button_screen_data == None:
            return False
        return True
    
    #Act: if condition_to_act is true, call draw
    def act(self, button_screen_data):
        if self.condition_to_act(button_screen_data):
            self.draw(button_screen_data)
        return
    
    #Draw: uses pygame's draw.rect function to draw a rectangle given screen and entity state
    #colors and bounds
    def draw(self, button_screen_data):
        pygame.draw.rect(button_screen_data, self.entity_state.color, self.entity_state.bounds)
        return