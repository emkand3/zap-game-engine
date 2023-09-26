#####   ACTIVATE ENTITY   #####
#Handles action for activating an entity. Type is "none"

class ActivateEntity:
    #Constructor
    def __init__(self):
        self.name = "activate_entity_action"
        self.types = ["none"]
        self.children = []
        self.entity_state = None
        self.verbose = False
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        return True

    #Act: if the action should should happen, set the entity_state.active from False to True
    def act(self):
        if self.condition_to_act():
            if self.entity_state.active == False:
                self.entity_state.active = True
        return