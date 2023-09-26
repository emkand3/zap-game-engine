#####   PARTICLE    #####
#Creates a list of particles to be handled.
#Constructor creates a list of position, velocity, acceleration,
#and mass, which are numbers given for each particle. Constructor
#creates a list of True/False to determine if the particle is active,
#and whether or not certain forces are acting on that particle. If set
#to True, the particle and forces are active, and if set to false,
#the particle and forces are inactive.

#NOTE: Although I had to change this class slightly to get my particles
#to fully function as expected, I feel that this way of doing the forces
#makes the most sense to me, as the active_particle list would serve the
#purpose of whether or not a particle should exist, and the specific force
#lists serve a function of whether or not certain forces are acting on a
#particular particle. That way, I can have certain forces acting differently
#upon particles, and still have the functionality to be able to remove particles
#if necessary.

class Particle:
    #Constructor
    def __init__(self, name):
        self.position = []
        self.velocity = []
        self.acceleration = []
        self.mass = []
        self.active_particle = []
        self.drag_force = []
        self.spring_force = []
        self.gravity_force = []
        self.actions = []
        self.name = name
        self.verbose = False
        self.active = True
        return
    
    #Insert Action: inserts action into entity's action list, and makes the action
    #have an entity state of itself.
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return
    
    #Add Particle: appends respective list with given starting values for a particle.
    def add_particle(self, p, v, m, d, s, g):
        self.position.append(p)
        self.velocity.append(v)
        self.acceleration.append([1.0, 0.0])
        self.mass.append(m)
        self.active_particle.append(True)
        self.drag_force.append(d)
        self.spring_force.append(s)
        self.gravity_force.append(g)