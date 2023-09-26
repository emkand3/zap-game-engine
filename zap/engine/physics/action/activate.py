#####   ACTIVATE FORCE    #####
#Action for handling whether or not a specific force is active.
#If type is 1, the force is spring. 2 for drag, 3 for gravity.
#Index is used to get the specific particle from the list.

class ActivatePhys:
    #Constructor
    def __init__(self, index, type):
        self.index = index
        self.type = type
        self.name = "activate_force_action"
        self.types = ["none"]
        self.children = []
        self.entity_state = None
        self.verbose = False
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, pos):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        #self.children[0] is is_inside. This is used so that activate and deactivate can be children of
        #pick_position, and minimal functionality needs to be added to the is_inside action. This line of
        #code checks to see if the particle with the given position is inside of the rectangle, and if so,
        #that specific particle's forces may be altered.
        if self.children[0].condition_to_act(pos):
            return True
        return False

    #Act: if the action should should happen, set the entity_state.active from False to True
    def act(self, pos):
        if self.condition_to_act(pos):
            #For each specific type of force, check in the list to see if the given particle's force is set
            #to false. If so, set that force to True.
            if self.type == 1: #spring
                if self.entity_state.spring_force[self.index] == False:
                    self.entity_state.spring_force[self.index] = True
            elif self.type == 2: #drag
                if self.entity_state.drag_force[self.index] == False:
                    self.entity_state.drag_force[self.index] = True
            elif self.type == 3: #gravity
                if self.entity_state.gravity_force[self.index] == False:
                    self.entity_state.gravity_force[self.index] = True
        return