#####   POSITION SOLVER    #####
#Action for solving position. Action is of type "physics"

class PositionSolve:
    #Constructor
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.dt = 1.0
        self.name = "position_solve_action"
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    #If action should happen, set entity_state's position to correct position
    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0, len(self.entity_state.position)):
                if self.entity_state.active_particle[i]:
                    self.entity_state.position[i][0] = self.entity_state.position[i][0] + self.dt * self.entity_state.velocity[i][0]
                    self.entity_state.position[i][1] = self.entity_state.position[i][1] + self.dt * self.entity_state.velocity[i][1]
            for c in self.children:
                c.act(self.entity_state)
        return
