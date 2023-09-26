#####     TERMINATE     #####
#Terminates the screen. Constructor sets type to "event".
import pygame

class Terminate:
    #Constructor
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "terminate_display"
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, kd):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if kd == None:
            return False
        return True

    #Act: if an action should happen, call terminate, passing a pygame event to it.
    def act(self, kd):
        if self.condition_to_act(kd):
            self.terminate(kd)
        return

    #Terminate: if kd (the event) is equal to clicking the x on the window, call
    #the terminate function from the entity state (screen). Likewise, if kd is a
    #key down event, and if that key is the escape key, call terminate from the
    #entity state (screen).
    def terminate(self, kd):
        if kd.type == pygame.QUIT:
            self.entity_state.terminate()
        if kd.type == pygame.KEYDOWN:
            if kd.key == pygame.K_ESCAPE:
                self.entity_state.terminate()
        return