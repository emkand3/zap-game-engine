##### IS INSIDE #####
#Action for checking if a position is inside of a rectangle.
#Type is none.

class IsInside:
    #Constructor
    def __init__(self):
        self.name = "is_inside_action"
        self.types = ["none"]
        self.entity_state = None
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen. Returns
    #self.entity_state.is_inside, which calls the entity_state's is_inside
    #action. If it is inside, return true. Otherwise, return false.
    def condition_to_act(self, pos):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return self.entity_state.is_inside(pos)
    
    #Act: If the position is inside of the rectangle, call the children of
    #this action.
    def act(self, pos):
        if self.condition_to_act(pos):
            for c in self.children:
                c.act()
        return