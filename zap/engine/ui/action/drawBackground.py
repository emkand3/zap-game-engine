import pygame

class DrawBackground:
    def __init__(self):
        self.name = "draw_background_img_action"
        self.types = ["display"]
        self.children = []
        self.entity_state = None
        self.verbose = False
    
    def condition_to_act(self, screen_data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if screen_data == None:
            return False
        return True
    
    def act(self, screen_data):
        if self.condition_to_act(screen_data):
            self.drawBkgd(screen_data)
    
    def drawBkgd(self, screen_data):
        imageRect = self.entity_state.image.get_rect()
        imageRect.left, imageRect.top = self.entity_state.location
        screen_data.blit(self.entity_state.image, imageRect)
        for c in self.children:
            c.act()