#####   START TIMER    #####
#Handles action to start/reset a timer. Type is "none"
import pygame

class StartTimer:
    #Constructor
    def __init__(self):
        self.name = "start_timer_action"
        self.types = ["none"]
        self.children = []
        self.entity_state = None
        self.verbose = False
        return
    
    #Condition To Act: checks to see if the action should happen. 
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    #Act: if action should happen, call startTimer()
    def act(self):
        if self.condition_to_act():
            self.startTimer()
    
    #Start Timer: uses pygames time.get_ticks() function to set the start_time of the entity_state to the current time in
    #ticks since the game has started
    def startTimer(self):
        self.entity_state.start_time = pygame.time.get_ticks()