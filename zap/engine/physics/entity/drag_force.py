#####   DRAG FORCE    #####
#Creates the drag force. Drag constant is changed in game file.

class DragForce:
    #Constructor
    def __init__(self, name):
        self.drag_constant = 0.1
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