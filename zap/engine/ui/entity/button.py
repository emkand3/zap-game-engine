#####   BUTTON    #####
#Creates a button. Constructor takes in bounds (position and size), color, and name of entity

class Button:
    #Constructor
    def __init__(self, bounds, color, name):
        self.xCoord = bounds[0]
        self.yCoord = bounds[1]
        self.xSize = bounds[2]
        self.ySize = bounds[3]
        self.bounds = [self.xCoord, self.yCoord, self.xSize, self.ySize]
        self.color = color
        self.name = name
        self.actions = []
        self.active = True
        return

    #Insert Action: allows an action to be added to the entity.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return
    
    #Is Inside: checks to see if a given position is contained within the bounds of the box
    def is_inside(self, pos):
        if pos[0] < self.bounds[0]:
            return False
        if pos[0] > self.bounds[2] + self.bounds[0]:
            return False
        if pos[1] < self.bounds[1]:
            return False
        if pos[1] > self.bounds[3] + self.bounds[1]:
            return False
        return True