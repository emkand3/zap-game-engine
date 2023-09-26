#####   TIMER   #####
#Creates a timer entity. Constructor takes in a name.
import pygame

class Timer:
    #Constructor
    def __init__(self, name):
        self.name = name
        self.actions = []
        self.active = True
        self.start_time = 0
        self.current_time = 0
    
    #Insert Action: allows an action to be added to the entity.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return
    
    #Tick: takes the current time, and sets it to the amount of ticks since pygame has been initialized.
    def tick(self):
        self.current_time = pygame.time.get_ticks()
        return
    
    #Elapsed Time: returns the current time minus the start time, getting the elapsed time.
    def elapsed_time(self):
        elapsed_time = self.current_time - self.start_time
        return elapsed_time