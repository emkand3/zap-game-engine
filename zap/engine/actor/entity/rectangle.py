#####       RECTANGLE       #####
#Creates a rectangle entity. The constructor takes in
#length, width, coordinates of where to place it, color,
#name, and whether or not it is filled. If filled is not
#set to 0, the rectangle will not be filled in, and will
#instead be a border of filled pixels

class Rectangle:
    #Constructor
    def __init__(self, length, width, coords, color, name, filled):
        self.length = length
        self.width = width
        self.filled = filled
        self.size = (self.length, self.width)
        self.coords = coords
        self.color = color
        self.name = name
        self.actions = []
        self.verbose = False
        self.active = True
        return

    #Insert Action: allows an action to be added to the entity.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return

    #Is inside: checks if given position is inside of rectangle
    def is_inside(self, pos):
        if pos[0] < self.coords[0]:
            return False
        if pos[0] > self.length + self.coords[0]:
            return False
        if pos[1] < self.coords[1]:
            return False
        if pos[1] > self.width + self.coords[1]:
            return False
        return True