#####   COUNTER     #####
#Creates a counter entity. Constructor takes in an initial value for the counter, and a name
class Counter:
    #Constructor
    def __init__(self, initVal, name):
        self.name = name
        self.counter = initVal
        self.actions = []
        self.active = True
        return
    
    #Insert Action: allows an action to be added to the entity.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return
    