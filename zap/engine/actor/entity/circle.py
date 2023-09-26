#####       CIRCLE ENTITY       #####
#Creates a circle entity. Constructor takes in 
#a radius (for size), color, name, and center (coordinates).

class Circle:
    #Constructor
    def __init__(self, radius, color, name, center):
        self.radius = radius
        self.color = color
        self.name = name
        self.position = center
        self.actions = []
        self.verbose = False
        self.active = True
        return
    
    #Insert Action: allows an action to be added to the entity.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return