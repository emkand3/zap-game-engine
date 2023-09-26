#####   SPRING FORCE ACTION    #####
#Action for computing spring force. Action is of type "force"

class SpringForceAction:
    #Constructor
    def __init__(self):
        self.types = ["force"]
        self.entity_state = None
        self.name = "spring_force_action"
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
    
    #Act: if the action should happen, compute spring force
    def act(self, data):
        if self.condition_to_act(data):
            total_mass = 0.1
            center_of_mass = [0.0, 0.0]
            for i in range(0, len(data.acceleration)):
                #check to make sure that only the correct particles are being included in the center_of_mass calculation
                if data.active_particle[i] and data.spring_force[i]:
                    total_mass = total_mass + data.mass[i]
                    center_of_mass[0] = center_of_mass[0] + data.mass[i] * data.position[i][0]
                    center_of_mass[1] = center_of_mass[1] + data.mass[i] * data.position[i][1]
            center_of_mass[0] = center_of_mass[0]/total_mass
            center_of_mass[1] = center_of_mass[1]/total_mass
            for i in range(0, len(data.acceleration)):
                #check to make sure that the particle you are adding spring to is both a particle that should exist, and a particle that
                #should have spring acting on it.
                if data.active_particle[i] and data.spring_force[i]:
                    accel = [0.0, 0.0]
                    accel[0] = (center_of_mass[0] - data.position[i][0]) * self.entity_state.spring_constant / data.mass[i]
                    accel[1] = (center_of_mass[1] - data.position[i][1]) * self.entity_state.spring_constant / data.mass[i]
                    data.acceleration[i][0] = data.acceleration[i][0] + accel[0]
                    data.acceleration[i][1] = data.acceleration[i][1] + accel[1]
            for c in self.children:
                c.act(data)