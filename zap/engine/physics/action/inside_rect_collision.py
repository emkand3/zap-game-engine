#####   INSIDE RECTANGLE COLLISION    #####
#Action for checking whether a particle should stay inside of a rectangle.

class InsideRectCollision:
    #Constructor
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.name = "inside_rect_collision"
        self.verbose = False
        self.children = []
        return
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True
    
    #Act: if action should happen, make sure particle stays within rectangle.
    def act(self, data):
        if self.condition_to_act(data):
            for i in range(0, len(data.position)):
                if data.active_particle[i]:
                    if data.position[i][0] < self.entity_state.llc[0]:
                        data.position[i][0] = 2.0*self.entity_state.llc[0] - data.position[i][0]
                        data.velocity[i][0] = -data.velocity[i][0]
                    elif data.position[i][0] > self.entity_state.urc[0]:
                        data.position[i][0] = 2.0*self.entity_state.urc[0] - data.position[i][0]
                        data.velocity[i][0] = -data.velocity[i][0]
                    elif data.position[i][1] < self.entity_state.llc[1]:
                        data.position[i][1] = 2.0*self.entity_state.llc[1] - data.position[i][1]
                        data.velocity[i][1] = -data.velocity[i][1]
                    elif data.position[i][1] > self.entity_state.urc[1]:
                        data.position[i][1] = 2.0*self.entity_state.urc[1] - data.position[i][1]
                        data.velocity[i][1] = -data.velocity[i][1]
            for c in self.children:
                c.act(data)