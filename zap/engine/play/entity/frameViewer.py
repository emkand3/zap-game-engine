#####       FRAME VIEWER        #####
#Creates a window. The constructor takes in the width and height in
#pixels, the background color, and the name of the screen.

import pygame

class FrameViewer:
    #Constructor
    def __init__ (self, width, height, color, name, mode):
        self.width = width
        self.height = height
        #self.mode = mode
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.color = color
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return
    
    #Insert Action: allows an action to be added to the entity.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return

    #Make Window: creates the actual window for display.
    def make_window(self):
        self.screen.fill(self.color, None)
        pygame.display.set_caption(self.name)
        return self.screen
    
    #Terminate: quits pygame, then exits the program.
    def terminate(self):
        from sys import exit
        pygame.quit()
        exit()