#####   ALARM   #####
#Handles alarm action. Type set to "none"

class Alarm:
    #Constructor
    def __init__(self, allottedTime):
        self.allottedTime = allottedTime
        self.name = "alarm_action"
        self.types = ["none"]
        self.children = []
        self.entity_state = None
        self.verbose = False
    
    #Condition To Act: checks to see if the action should happen. 
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    #Act: if the action should should happen, call self.activateAlarm()
    def act(self):
        if self.condition_to_act():
            self.activateAlarm()
    
    #Activate Alarm: finds the elapsed time from the entity state. If that time is larger than the allotted time given in the
    #constructor, call all children actions apart of alarm.
    def activateAlarm(self):
        elapsed_time = self.entity_state.elapsed_time()
        if elapsed_time >= self.allottedTime:
            if self.verbose == True:
                print(self.name + " being set off")
            for c in self.children:
                if self.verbose == True:
                    print(c)
                c.act()