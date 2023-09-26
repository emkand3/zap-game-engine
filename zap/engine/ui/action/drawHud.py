#####   DRAW HUD    #####
#Handles action for drawing hud. Type set to "display"
import pygame

class DrawHud:
    #Constructor
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.name = "draw_hud_action"
        self.children = []
        self.verbose = False
        return

    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, hud_screen_data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if hud_screen_data == None:
            return False
        return True
    
    #Act: if condition_to_act is true, calls displayHud
    def act(self, hud_screen_data):
        if self.condition_to_act(hud_screen_data):
            self.displayHud(hud_screen_data)
        return
    
    #Display Hud: creates a font using entity_state's fontsize, then creates two strings given by the
    #entity_state's append_string method. Then, uses the render() function to allow those strings to be
    #printed out with the entity_state's color, and blits them to the screen at their given coords.
    def displayHud(self, hud_screen_data):
        wordString = pygame.font.Font(self.entity_state.font, self.entity_state.fontsize)
        ap1 = self.entity_state.append_string(self.entity_state.firstString, self.entity_state.numAppeared)
        ap2 = self.entity_state.append_string(self.entity_state.secondString, self.entity_state.numSuccess)
        text1 = wordString.render(ap1, True, self.entity_state.color)
        text2 = wordString.render(ap2, True, self.entity_state.color)
        hud_screen_data.blit(text1, self.entity_state.coords1)
        hud_screen_data.blit(text2, self.entity_state.coords2)
        if self.verbose:
            print(ap1)
            print(ap2)
        return
