import pygame

class Background:
    def __init__(self, image, location, name):
        self.image = pygame.image.load(image)
        self.location = location
        self.name = name
        self.active = True
        self.actions = []
        return

    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return