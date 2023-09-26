#####   COUNTER INCREMENT   #####
#Handles action for incrementing a counter by 1. Type is "none"

class CounterIncrement:
    #Constructor
    def __init__(self):
        self.name = "counter_increment_action"
        self.types = ["none"]
        self.children = []
        self.entity_state = None
        self.verbose = False
        return
    
    #Condition To Act: checks to see if the action should happen. 
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    #Act: if the action should should happen, add 1 to the entity_state.counter variable, then call all children action
    def act(self):
        if self.condition_to_act():
            self.entity_state.counter += 1
            for c in self.children:
                if self.verbose:
                    print(c)
                c.act()