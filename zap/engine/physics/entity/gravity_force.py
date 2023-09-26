#####   GRAVITY FORCE   #####
#Creates the gravity force. Gravity constants are changed in game file.

class GravityForce:
    #Constructor
    def __init__(self, name):
        self.gravity = [0.0, -1.0]
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