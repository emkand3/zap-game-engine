####    EULER SOLVER    #####
#Action for solving position and velocity. Action is of type "physics"

class EulerSolve:
    #Constructor
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.dt = 1.0
        self.name = "euler_solver_action"
        self.verbose = False
        self.children = []
        return

    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if len(self.children) < 2:
            return False
        return True
    
    #If the action should happen, compute euler solver
    def act(self):
        if self.condition_to_act():
            self.children[0].dt = float(self.dt)
            self.children[1].dt = float(self.dt)
            self.children[0].act(self.entity_state)
            self.children[1].act(self.entity_state)
            for c in self.children[2:]:
                c.act(self.entity_state)