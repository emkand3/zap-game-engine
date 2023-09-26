#####   DRAG FORCE ACTION    #####
#Action for computing drag force. Type is set to "force"

class DragForceAction:
    #Constructor
    def __init__(self):
        self.types = ["force"]
        self.entity_state = None
        self.name = "drag_force_action"
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True
    
    #Act: if action should happen, compute the drag force
    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0, len(data.acceleration)):
                #check to make sure that the particle you are adding drag to is both a particle that should exist, and a particle that
                #should have drag acting on it.
                if data.active_particle[i] and data.drag_force[i]:
                    data.acceleration[i][0] = data.acceleration[i][0] - data.velocity[i][0] * self.entity_state.drag_constant
                    data.acceleration[i][1] = data.acceleration[i][1] - data.velocity[i][1] * self.entity_state.drag_constant
            for c in self.children:
                c.act(data)