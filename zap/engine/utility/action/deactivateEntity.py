#####   DEACTIVATE ENTITY   #####
#Handles action to deactivate an entity. Type is "none"

class DeactivateEntity:
    #Constructor
    def __init__(self):
        self.name = "deactivate_entity_action"
        self.types = ["none"]
        self.children = []
        self.entity_state = None
        self.verbose = False
    
    #Condition To Act: checks to see if the action should happen. 
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        return True

    #Act: if the action should happen, set the entity_state.active from True to False
    def act(self):
        if self.condition_to_act():
            if self.entity_state.active == True:
                self.entity_state.active = False
        return