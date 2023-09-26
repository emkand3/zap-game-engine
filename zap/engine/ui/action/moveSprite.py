import pygame

class MoveSprite:
    def __init__(self):
        self.name = "move_sprite_action"
        self.types = ["keydown"]
        self.children = []
        self.entity_state = None
        self.verbose = False
        return
    
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        #if event.type == pygame.KEYDOWN:
        #    return True
        return True

    def act(self, keys):
        if self.condition_to_act():
            if keys[pygame.K_LEFT]:
                self.entity_state.move_left(2)
                for c in self.children:
                    c.group.update()
            if keys[pygame.K_RIGHT]:
                self.entity_state.move_right(2)
                for c in self.children:
                    c.group.update()
            if not keys:
                self.entity_state.image = self.entity_state.images[0]
