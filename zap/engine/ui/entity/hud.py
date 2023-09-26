#####   HUD   #####
#Creates hud entity. Constructor takes in color of text, coords of first and second strings, font size, and
#strings representing the first string to by typed and the second string to be typed. Constructor also has
#class variables representing the number of times appeared, and the number of successes.
class Hud:
    #Constructor
    def __init__(self, color, coords1, coords2, fontsize, firstString, secondString, font):
        self.color = color
        self.coords1 = coords1
        self.coords2 = coords2
        self.fontsize = fontsize
        self.actions = []
        self.active = True
        self.firstString = firstString
        self.secondString = secondString
        self.numAppeared = 0
        self.numSuccess = 0
        self.name = "hud"
        self.font = font
        return
    
    #Insert Action: allows an action to be added to the entity.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return
    
    #Append String: allows string and number to be appended into one string
    def append_string(self, fString, num):
        newString = fString + " " + str(num)
        return newString
    