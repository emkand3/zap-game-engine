#####   PICK POSITION   #####
#Action to get position of particle. Action is of type "position"

class PickPosition:
    #Constructor
    def __init__(self, index):
        self.types = ["position"]
        self.particle_index = index
        self.entity_state = None
        self.name = "pick_position_action"
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if self.particle_index >= len(self.entity_state.position):
            return False
        if self.entity_state.active_particle[self.particle_index] == False:
            return False
        return True
    
    #Act: If action should happen, get position of particle and send it to children
    def act(self, data):
        if self.condition_to_act(data):
            new_data = list(self.entity_state.position[self.particle_index])
            for c in self.children:
                c.act(new_data)
        return