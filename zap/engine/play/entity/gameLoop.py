#####       GAME LOOP       #####
#Creates game loop. Constructor takes in name of the loop.

import pygame

class GameLoop:
    #Constructor
    def __init__(self, name):
        self.event_action = []
        self.loop_action = []
        self.display_action = []
        self.keydown_action = []
        self.name = name
        self.verbose = False
        self.active = True
        self.clock = pygame.time.Clock()
        return

    #Insert Entity: allows entities to be added to loop, and will then
    #search those entities for their specific actions.
    def insert_entity(self, entity):
        for e in entity:
            for action in e.actions:
                self.insert_action(action)
        return
    
    #Insert Action: finds all actions in specific entity, and adds them
    #to the list corresponding to the type of action.
    def insert_action(self, action):
        if "event" in action.types:
            self.event_action.append(action)
        elif "loop" in action.types:
            self.loop_action.append(action)
        elif "displayA" in action.types:
            if self.verbose:
                print("display added to " + self.name)
            self.display_action.append(action)
        elif "keydown" in action.types:
            self.keydown_action.append(action)
        return

    #Loop: infinite loop of the game. Checks for any events happening during
    #the game, then passes those events into its event_action list.
    def loop(self):
        self.clock.tick(1)
        while self.active:
            for ev in pygame.event.get():
                for action in self.event_action:
                    action.act(ev)
            for action in self.loop_action:
                action.act()
            for action in self.display_action:
                action.act()
            for action in self.keydown_action:
                keys = pygame.key.get_pressed()
                action.act(keys)
        return