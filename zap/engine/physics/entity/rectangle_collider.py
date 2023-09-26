#####   RECTANGLE COLLLIDER    #####
#Creates rectangle collision entity. Constructor takes in the position
#of the llc, urc, and the name of the collider.

class RectangleCollider:
    #Constructor
    def __init__(self, llc, urc, name):
        self.llc = llc
        self.urc = urc
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return
    
    #Insert Action: inserts action into entity's action list, and makes the action
    #have an entity state of itself.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return