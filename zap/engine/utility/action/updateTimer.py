#####   UPDATE TIMER    #####
#Handles action for updating the current timer. Type is "loop"

class UpdateTimer:
    #Constructor
    def __init__(self):
        self.name = "update_timer_action"
        self.types = ["loop"]
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
    
    #Act: if the action should happen, call updateTimer, then call all children in update timer
    def act(self):
        if self.condition_to_act():
            self.updateTimer()
            for c in self.children:
                if self.verbose:
                    print(c)
                c.act()
    
    #Update Timer: calls tick method from the entity state.
    def updateTimer(self):
        self.entity_state.tick()
        if self.verbose:
            print(self.entity_state.current_time)