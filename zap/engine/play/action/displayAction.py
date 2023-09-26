#####   DISPLAY ACTION  #####
#Handles actions of type display. Constructor sets type to "display".

import pygame

class DisplayAction:
    #Constructor
    def __init__(self):
        self.types = ["displayA"]
        self.entity_list = []
        self.entity_state = None
        self.name = "display_action"
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    #Act: if the action should happen, call display
    def act(self):
        if self.condition_to_act():
            self.display()
        return

    #Add Entity: add an entity to the entity list of display
    def add_entity(self, entity):
        self.entity_list.append(entity)
        return

    #Display: sets the screen to black, loops through all of the entities in
    #display action object, then acts on those actions, passing the screen to
    #each. Finally, updates the display.
    def display(self):
        self.entity_state.screen.fill((0, 0, 0))
        for ent in self.entity_list:
            for a in ent.actions:
                if (a.types[0] == "display") and (ent.active == True):
                    a.act(self.entity_state.screen)
        pygame.display.update()
        return