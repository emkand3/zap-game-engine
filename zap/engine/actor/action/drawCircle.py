#####   DRAW CIRCLE     #####
#Action to draw a circle. Constructor sets type as "display".
import pygame

class DrawCircleAction:
    #Constructor
    def __init__(self):
        self.name = "draw_circle_action"
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        return

    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, circle_screen_data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            print("inactive")
            return False
        if circle_screen_data == None:
            return False
        return True
    
    #Act: if the action should happen, calls draw, passing in the screen to be
    #drawn on.
    def act(self, circle_screen_data):
        if self.condition_to_act(circle_screen_data):
            self.draw(circle_screen_data)
        return
    
    #Draw: draws a circle using pygame's draw.circle method. Uses the Circle entity_state
    #that the action is attached to and gets color, center, and radius.
    def draw(self, screen):
        pygame.draw.circle(screen, self.entity_state.color, self.entity_state.position, self.entity_state.radius)
        if self.verbose:
            print("drawing circle...")
        return