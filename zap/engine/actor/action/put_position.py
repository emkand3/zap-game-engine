#####   PUT POSITION    #####
#Puts the given position onto this action's
#entity state's position. Action is of type "position"

class PutPosition:
    #Constructor
    def __init__(self, index):
        self.types = ["position"]
        self.index = index
        self.entity_state = None
        self.name = "put_position_action"
        self.verbose = False
        self.children = []
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if self.entity_state.active == False:
            return False
        if len(data) != 2:
            return False
        return True
    
    #Act: if the action should happen, set the entity state's position
    #to the data passed into the act function, then call all children.
    def act(self, data):
        if self.condition_to_act(data):
            self.entity_state.position = list(data)
            for c in self.children:
                c.act(data)