#####   SPRING FORCE    #####
#Creates a spring force entity. Spring constant is set in
#game file.

class SpringForce:
    #Constructor
    def __init__(self, name):
        self.spring_constant = 1.0
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