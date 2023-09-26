#####   GRAVITY FORCE ACTION    #####
#Action for computing gravity force. Type is set to "force"


class GravityForceAction:
    #Constructor
    def __init__(self):
        self.types = ["force"]
        self.entity_state = None
        self.name = "gravity_force_action"
        self.verbose = False
        self.children = []
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True
    
    #Act: if action should happen, compute the gravity force
    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0, len(data.acceleration)):
                #check to make sure that the particle you are adding gravity to is both a particle that should exist, and a particle that
                #should have gravity acting on it.
                if data.active_particle[i] and data.gravity_force[i]:
                    data.acceleration[i][0] = data.acceleration[i][0] + self.entity_state.gravity[0]
                    data.acceleration[i][1] = data.acceleration[i][1] + self.entity_state.gravity[1]
            for c in self.children:
                c.act(data)